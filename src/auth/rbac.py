from typing import Annotated

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session

from db.conn import get_session
from models import Role
from auth.security import decode_access_token, oauth2_scheme


class UserCreateRequestWithRole(BaseModel):
    username: str
    email: EmailStr
    role: Role


def get_current_user(
    token: str = Depends(oauth2_scheme),
    session: Session = Depends(get_session),
) -> UserCreateRequestWithRole:
    user = decode_access_token(token, session)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not authorized",
        )

    return UserCreateRequestWithRole(
        username=user.username,
        email=user.email,
        role=user.role,
    )


def get_admin_user(
    current_user: Annotated[
        get_current_user, Depends()
    ],
):
    if current_user.role != Role.admin:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not authorized",
        )
    return current_user


router = APIRouter()


@router.get(
    "/welcome/all-users",
    responses={
        status.HTTP_401_UNAUTHORIZED: {
            "description": "User not authorized"
        }
    },
)
def all_user_can_access(
    user: Annotated[get_current_user, Depends()],
):
    return {
        f"Hello {user.username}, welcome to the basic user endpoint"
    }


@router.get(
    "/welcome/admin-only",
    responses={
        status.HTTP_401_UNAUTHORIZED: {
            "description": "User not authorized"
        }
    },
)
def only_admin_can_access(
    user: Annotated[get_admin_user, Depends()],
):
    return {
        f"Hello {user.username}, "
        "welcome to the admin endpoint"
    }
