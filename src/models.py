from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    # full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    provider_type = Column(String)
    provider_id = Column(Integer, unique=True)
    is_super_user = Column(Boolean, default=False)

    profiles = relationship("UserProfile", back_populates="user")


class UserProfile(Base):
    __tablename__ = "userprofile"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    first_name = Column(String)
    last_name = Column(String)

    user = relationship("User", back_populates="profiles")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    # owner = relationship("User", back_populates="items")
