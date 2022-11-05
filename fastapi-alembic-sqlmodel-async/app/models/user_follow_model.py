from uuid import UUID
from typing import Optional

from app.models.base_uuid_model import BaseUUIDModel, SQLModel
from sqlmodel import Column, Field, Boolean


class UserFollowBase(SQLModel):
    user_id: UUID = Field(nullable=False)
    target_user_id: UUID = Field(nullable=False)


class UserFollow(BaseUUIDModel, UserFollowBase, table=True):
    is_mutual: Optional[bool] = Field(sa_column=Column(Boolean(), server_default="0"))
