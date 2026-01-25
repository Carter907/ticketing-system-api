from typing import Annotated

from pydantic import BaseModel, EmailStr, Field

from models import Priority, Status


class UserCreateBody(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserCreateResponse(BaseModel):
    username: str
    email: EmailStr


class ResponseCreateUser(BaseModel):
    message: Annotated[
        str, Field(default="user created")
    ]
    user: UserCreateResponse


class TicketCreateBody(BaseModel):
    subject: str
    description: str
    owner: str
    priority: Priority = Priority.medium
    status: Status = Status.not_started


class TicketCreateResponse(BaseModel):
    subject: str
    description: str
    owner: str
    priority: Priority
    status: Status


class ResponseCreateTicket(BaseModel):
    message: Annotated[
        str, Field(default="ticket created")
    ]
    ticket: TicketCreateResponse


class ResponseGetAllTickets(BaseModel):
    message: Annotated[
        str, Field(default="tickets retrieved")
    ]
    tickets: list[TicketCreateResponse]
