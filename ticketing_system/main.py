from fastapi import FastAPI
from ticketing_system.model.ticket import Ticket
from ticketing_system.data.mock_data import tickets

app = FastAPI()


# create a ticket
@app.post("/tickets/create")
def create_ticket(ticket: Ticket) -> Ticket:
    tickets().append(ticket)
    return ticket


# get all tickets
@app.get("/tickets")
def get_all_tickets() -> list[Ticket]:
    return tickets()
