from typing import List, Optional

from pydantic import BaseModel, EmailStr

############# Item Schema ###############
class ItemBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None

# Properties to receive on item creation
class ItemCreate(ItemBase):
    title: str

# Properties to receive on item update
class ItemUpdate(ItemBase):
    pass

# Properties shared by models stored in DB
class ItemInDBBase(ItemBase):
    id: int
    title: str
    owner_id: int

    class Config:
        orm_mode = True

# Properties to return to client
class Item(ItemInDBBase):
    """docstring for Item."""
    pass

# Properties properties stored in DB
class ItemInDB(ItemInDBBase):
    pass


#################### User Schema #####################

class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = True
    # full_name: Optional[str] = None
    provider_type: Optional[str] = None
    provider_id: Optional[int] = None
    is_super_user: Optional[bool] = False

# Properties to receive via API on creation
class UserCreate(UserBase):
    email: EmailStr
    hashed_password: str

class UserInDBBase(UserBase):
    """docstring for UserInDBBase."""

    id: Optional[int] = None
    class Config:
        orm_mode = True

# Additional properties to return via API
class User(UserInDBBase):
    pass

# Additional properties stored in DB
class UserInDB(UserInDBBase):
    hashed_password: str

############## User Profile ###############
class UserProfileBase(BaseModel):
    user_id: Optional[int] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None

# Properties to receive via API on creation
class UserProfileCreate(UserProfileBase):
    first_name: EmailStr
    last_name: str

class UserProfileInDBBase(UserProfileBase):

    id: Optional[int] = None
    class Config:
        orm_mode = True

# Additional properties to return via API
class UserProfile(UserProfileInDBBase):
    pass


########### Token #############
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenPayload(BaseModel):
    sub: Optional[int] = None


############Message ###################
class Msg(BaseModel):
    msg: str
