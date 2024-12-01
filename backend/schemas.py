from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import List, Optional

class UserBase(BaseModel):
    email: EmailStr
    name: str
    avatar_url: Optional[str] = None
    bio: Optional[str] = None
    created_at: Optional[datetime] = datetime.utcnow()


class UserCreate(UserBase):
    google_id: str


class User(UserBase):
    id: int
    google_id: str

    class Config:
        orm_mode = True

class PortfolioBase(BaseModel):
    title: str
    description: Optional[str] = None


class PortfolioCreate(PortfolioBase):
    pass


class Portfolio(PortfolioBase):
    id: int
    user_id: int
    created_at: datetime

    class Config:
        orm_mode = True


# Tag Schemas
class TagBase(BaseModel):
    name: str


class TagCreate(TagBase):
    pass


class Tag(TagBase):
    id: int

    class Config:
        orm_mode = True


class CommentBase(BaseModel):
    content: str
    rating: Optional[int] = None


class CommentCreate(CommentBase):
    portfolio_id: int
    user_id: int


class Comment(CommentBase):
    id: int
    portfolio_id: int
    user_id: int
    created_at: datetime

    class Config:
        orm_mode = True


class SectionCategoryBase(BaseModel):
    title: str
    description: Optional[str] = None


class SectionCategoryCreate(SectionCategoryBase):
    pass


class SectionCategory(SectionCategoryBase):
    id: int
    portfolio_id: int
    created_at: datetime

    class Config:
        orm_mode = True


class SectionLinkBase(BaseModel):
    link_url: str


class SectionLinkCreate(SectionLinkBase):
    section_id: int


class SectionLink(SectionLinkBase):
    id: int
    section_id: int
    created_at: datetime

    class Config:
        orm_mode = True
