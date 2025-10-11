from ticket_system.model.ticket import Ticket

ticketList: list[Ticket] = [
    Ticket(
        id=1,
        subject="Ticket 1",
        description="Description for Ticket 1",
        status="not started",
    ),
    Ticket(
        id=2,
        subject="Ticket 2",
        description="Description for Ticket 2",
        status="in progress",
    ),
    Ticket(
        id=3,
        subject="Ticket 3",
        description="Description for Ticket 3",
        status="completed",
    ),
    Ticket(
        id=4,
        subject="Ticket 4",
        description="Description for Ticket 4",
        status="not started",
    ),
    Ticket(
        id=5,
        subject="Ticket 5",
        description="Description for Ticket 5",
        status="in progress",
    ),
    Ticket(
        id=6,
        subject="Ticket 6",
        description="Description for Ticket 6",
        status="completed",
    ),
]


def tickets() -> list[Ticket]:
    return ticketList
