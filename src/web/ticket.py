from fastapi.routing import APIRouter
from data.mock_data import tickets
from model.ticket import Ticket
from fastapi import Depends, HTTPException


router = APIRouter(prefix="/tickets")


@router.post("/create")
async def create_ticket(ticket: Ticket) -> Ticket:
    tickets().append(ticket)
    return ticket


@router.get("/")
async def get_all_tickets() -> list[Ticket]:
    return tickets()

@router.get("/{ticket_id}")
async def get_ticket(ticket_id: int) -> list[Ticket]:
    if ticket_id not in tickets():
        raise HTTPException(status_code=404, detail=f"Ticket not found with id {ticket_id}");
    
    return tickets()[ticket_id]
