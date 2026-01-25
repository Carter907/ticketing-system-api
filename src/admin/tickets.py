from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from db.conn import get_session
from operations import add_ticket, get_all_tickets
from auth.rbac import get_admin_user
from responses import (
    ResponseCreateTicket,
    ResponseGetAllTickets,
    TicketCreateBody,
    TicketCreateResponse,
)

router = APIRouter(prefix="/tickets")


@router.post(
    "/create",
    status_code=status.HTTP_201_CREATED,
    response_model=ResponseCreateTicket,
    responses={
        status.HTTP_409_CONFLICT: {
            "description": "The ticket already exists"
        },
        status.HTTP_401_UNAUTHORIZED: {
            "description": "User not authorized"
        },
    },
)
def create_ticket(
    ticket: TicketCreateBody,
    user: Annotated[get_admin_user, Depends()],
    session: Session = Depends(get_session),
) -> dict[str, TicketCreateResponse]:
    db_ticket = add_ticket(
        session=session, **ticket.model_dump()
    )
    if not db_ticket:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="ticket already exists",
        )
    ticket_response = TicketCreateResponse(
        subject=db_ticket.subject,
        description=db_ticket.description,
        owner=db_ticket.owner,
        priority=db_ticket.priority,
        status=db_ticket.status,
    )
    return {
        "message": "ticket created",
        "ticket": ticket_response,
    }


@router.get(
    "/all",
    response_model=ResponseGetAllTickets,
    responses={
        status.HTTP_401_UNAUTHORIZED: {
            "description": "User not authorized"
        },
    },
)
def get_all_tickets_for_admins(
    user: Annotated[get_admin_user, Depends()],
    session: Session = Depends(get_session),
) -> dict[str, list[TicketCreateResponse]]:
    db_tickets = get_all_tickets(session=session)
    ticket_responses = [
        TicketCreateResponse(
            subject=ticket.subject,
            description=ticket.description,
            owner=ticket.owner,
            priority=ticket.priority,
            status=ticket.status,
        )
        for ticket in db_tickets
    ]
    return {
        "message": "tickets retrieved",
        "tickets": ticket_responses,
    }
