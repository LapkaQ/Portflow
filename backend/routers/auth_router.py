from fastapi import APIRouter, Request, Depends
from starlette.responses import JSONResponse, RedirectResponse
from services.auth_services import oauth
from authlib.integrations.starlette_client import OAuthError
from database import get_db
from services.user_services import create_or_get_user
from sqlalchemy.orm import Session
from schemas import UserCreate
from config import settings

router = APIRouter()

@router.get("/login", response_class=JSONResponse)
async def login(request: Request):
    url = request.url_for('auth')
    return await oauth.google.authorize_redirect(request, url)

@router.get('/auth', response_class=JSONResponse)
async def auth(request: Request, db: Session = Depends(get_db)):
    try:
        token = await oauth.google.authorize_access_token(request)
    except OAuthError as e:
        return JSONResponse(content={"error": e.error}, status_code=400)

    user_info = token.get('userinfo')
    if user_info:
        user_create = UserCreate(
            google_id=user_info['sub'],
            email=user_info['email'],
            name=user_info['name'],
            avatar_url=user_info.get('picture', None),
            bio=user_info.get('bio', None)
        )

        user = create_or_get_user(db, user_create)
        
        request.session['user'] = {
            "id": user.id,
            "google_id": user.google_id,
            "email": user.email,
            "name": user.name,
            "avatar_url": user.avatar_url,
            "bio": user.bio,
        }

        response = JSONResponse(content={
            "message": "User logged in successfully",
            "user": request.session['user'],
            "redirect": settings.FRONTEND_APP_URL
        })
        response.set_cookie("user", request.session["user"]["id"], httponly=True, secure=False, path="/")

        return response

