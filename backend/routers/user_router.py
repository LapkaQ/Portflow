from fastapi import APIRouter, Request
from starlette.responses import JSONResponse
from services.user_services import get_user_data
from config import settings

router = APIRouter()

@router.get("/", response_class=JSONResponse)
def index(request: Request):
    user = request.session.get('user')
    if user:
        return JSONResponse(content={"message": "User is logged in", "redirect": settings.FRONTEND_APP_URL})
    return JSONResponse(content={"message": "User is not logged in", "redirect": settings.FRONTEND_APP_URL})

@router.get('/welcome', response_class=JSONResponse)
def welcome(request: Request):
    user = request.session.get('user')
    if not user:
        return JSONResponse(content={"error": "Unauthorized", "redirect": settings.FRONTEND_APP_URL}, status_code=401)
    return JSONResponse(content={"message": "Welcome", "user": user})

@router.get('/logout', response_class=JSONResponse)
def logout(request: Request):
    request.session.pop('user', None)
    request.session.clear()
    return JSONResponse(content={"message": "Logged out", "redirect": settings.FRONTEND_APP_URL})

@router.get("/user", response_class=JSONResponse)
def get_user(request: Request):
    user = request.session.get("user")
    if not user:
        return JSONResponse(content={"error": "Unauthorized"}, status_code=401)
    user_data = get_user_data(user)
    return JSONResponse(content={"user": user_data})
