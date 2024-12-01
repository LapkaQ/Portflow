from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, Boolean, Enum, Table
from sqlalchemy.orm import relationship
from database import Base
import enum

LENGTH_SHORT = 20
LENGTH_CODE = 64
LENGTH_NAME = 256
LENGTH_DESCRIPTION = 512

class LinkType(enum.Enum):
    VIDEO = "video"
    CHANNEL = "channel"
    THUMBNAIL = "thumbnail"

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    google_id = Column(String(LENGTH_NAME), unique=True, nullable=False)
    email = Column(String(LENGTH_NAME), unique=True, nullable=False)
    name = Column(String(LENGTH_NAME), nullable=False)
    avatar_url = Column(Text, nullable=True)
    bio = Column(Text, nullable=True)
    created_at = Column(DateTime, nullable=False)

    portfolio = relationship("Portfolio", back_populates="user", uselist=False)

class Portfolio(Base):
    __tablename__ = 'portfolios'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    title = Column(String(LENGTH_NAME), nullable=False)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime, nullable=False)

    user = relationship("User", back_populates="portfolio")
    tags = relationship("PortfolioTag", back_populates="portfolio")
    comments = relationship("Comment", back_populates="portfolio")
    sections = relationship("SectionCategory", back_populates="portfolio")

class Tag(Base):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(LENGTH_NAME), unique=True, nullable=False)

    portfolio_tags = relationship("PortfolioTag", back_populates="tag")

class PortfolioTag(Base):
    __tablename__ = 'portfolio_tags'

    id = Column(Integer, primary_key=True, index=True)
    portfolio_id = Column(Integer, ForeignKey('portfolios.id'), nullable=False)
    tag_id = Column(Integer, ForeignKey('tags.id'), nullable=False)

    portfolio = relationship("Portfolio", back_populates="tags")
    tag = relationship("Tag", back_populates="portfolio_tags")

class Comment(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True, index=True)
    portfolio_id = Column(Integer, ForeignKey('portfolios.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    content = Column(Text, nullable=False)
    rating = Column(Integer, nullable=True)
    created_at = Column(DateTime, nullable=False)

    portfolio = relationship("Portfolio", back_populates="comments")

class SectionCategory(Base):
    __tablename__ = 'section_categories'

    id = Column(Integer, primary_key=True, index=True)
    portfolio_id = Column(Integer, ForeignKey('portfolios.id'), nullable=False)
    title = Column(String(LENGTH_NAME), nullable=False)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime, nullable=False)

    portfolio = relationship("Portfolio", back_populates="sections")
    links = relationship("SectionLink", back_populates="section")

class SectionLink(Base):
    __tablename__ = 'section_links'

    id = Column(Integer, primary_key=True, index=True)
    section_id = Column(Integer, ForeignKey('section_categories.id'), nullable=False)
    link_url = Column(Text, nullable=False)
    type = Column(Enum(LinkType, native_enum=False, length=LENGTH_CODE), nullable=False)
    created_at = Column(DateTime, nullable=False)

    section = relationship("SectionCategory", back_populates="links")
