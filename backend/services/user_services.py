from sqlalchemy.orm import Session
from datetime import datetime
from models import User
from schemas import UserCreate

def get_user_data(user):
    return {
        "name": user.get('name'),
        "email": user.get('email'),
        "avatar_rul": user.get('avatar_url'),
        "user_id": user.get('id')
    }

def create_or_get_user(db: Session, user_create: UserCreate):
    user = db.query(User).filter(User.google_id == user_create.google_id).first()
    
    if not user:
        user = User(
            google_id=user_create.google_id,
            email=user_create.email,
            name=user_create.name,
            avatar_url=user_create.avatar_url,
            bio=user_create.bio,
            created_at=datetime.utcnow()
        )
        db.add(user)
        db.commit()
        db.refresh(user)

    return user