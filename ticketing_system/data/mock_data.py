from ticketing_system.model.ticket import Ticket

ticketList: list[Ticket] = []


def tickets() -> list[Ticket]:
    return ticketList
