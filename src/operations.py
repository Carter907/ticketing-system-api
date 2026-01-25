from email_validator import (
    EmailNotValidError,
    validate_email,
)
from passlib.context import CryptContext
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from models import Role, User, Ticket, Status, Priority

pwd_context = CryptContext(
    schemes=["bcrypt"], deprecated="auto"
)


def add_user(
    session: Session,
    username: str,
    password: str,
    email: str,
    role: Role = Role.basic,
) -> User | None:
    hashed_password = pwd_context.hash(password)
    db_user = User(
        username=username,
        email=email,
        hashed_password=hashed_password,
        role=role,
    )
    session.add(db_user)
    try:
        session.commit()
        session.refresh(db_user)
    except IntegrityError:
        session.rollback()
        return None
    return db_user


def get_user(
    session: Session, username_or_email: str
) -> User | None:
    try:
        validate_email(username_or_email)
        query_filter = User.email
    except EmailNotValidError:
        query_filter = User.username
    user = (
        session.query(User)
        .filter(query_filter == username_or_email)
        .first()
    )
    return user

def add_ticket(
    session: Session,
    subject: str,
    description: str,
    owner: str,
    priority: Priority,
    status: Status,
) -> User | None:

    db_ticket = Ticket(
        subject=subject,
        description=description,
        owner=owner,
        priority=priority,
        status=status,
    )
    session.add(db_ticket)
    try:
        session.commit()
        session.refresh(db_ticket)
    except IntegrityError:
        session.rollback()
        return None
    return db_ticket

def get_ticket(
    session: Session, subject: str
) -> Ticket | None:
    query_filter = Ticket.subject

    ticket = (
        session.query(Ticket)
        .filter(query_filter == subject)
        .first()
    )
    return ticket


def get_all_tickets(
    session: Session,
) -> list[Ticket]:
    tickets = session.query(Ticket).all()
    return tickets
