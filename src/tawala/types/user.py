# app/schemas/user.py
from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional
from uuid import UUID
from datetime import datetime

class UserBase(BaseModel):
    email: EmailStr
    name: Optional[str]
    role: Optional[str]
    is_active: Optional[bool] = True

class UserCreate(UserBase):
    # password: str
    organization_id: UUID

class UserUpdate(BaseModel):
    email: Optional[EmailStr]
    name: Optional[str]
    role: Optional[str]
    is_active: Optional[bool]

class UserRead(UserBase):
    id: UUID
    # organization_id: UUID
    email: EmailStr
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)