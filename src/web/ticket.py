from fastapi.routing import APIRouter
from data.mock_data import tickets
from model.ticket import Ticket

router = APIRouter(prefix="/tickets")


# create a ticket
@router.post("/create")
def create_ticket(ticket: Ticket) -> Ticket:
    tickets().append(ticket)
    return ticket


# get all tickets
@router.get("/")
def get_all_tickets() -> list[Ticket]:
    return tickets()
