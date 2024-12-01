from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware
from fastapi.middleware.cors import CORSMiddleware
from routers import auth_router, user_router
from services.auth_services import oauth
from config import settings

app = FastAPI()

app.add_middleware(SessionMiddleware, secret_key=settings.SECRET_KEY)
app.include_router(auth_router.router)
app.include_router(user_router.router)

oauth.register(
    name='google',
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_id=settings.GOOGLE_CLIENT_ID,
    client_secret=settings.GOOGLE_CLIENT_SECRET,
    client_kwargs={
        'scope': 'email openid profile',
        'redirect_url': f'{settings.GOOGLE_REDIRECT_URL}'
    }
)
origins = [
    settings.FRONTEND_APP_URL,
    "http://localhost:5173",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)