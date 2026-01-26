# Roadmap

## Project Overview

This project is a ticketing system API built with FastAPI. It provides functionalities for user registration, authentication, ticket management, and role-based access control.

## Current Features

### User Management
- [x] User registration for regular users.
- [x] User registration for admin users.
- [x] User login and logout.
- [x] Get current user information.

### Ticket Management
- [x] Create tickets (admin only).
- [x] Get all tickets (admin only).

### Authentication and Authorization
- [x] Token-based authentication.
- [x] Role-based access control (RBAC).
- [x] Endpoints for all authenticated users.
- [x] Endpoints for admin users only.

## Partially Implemented

### Ticket Management
- [ ] Get ticket by ID (currently implemented by subject).

## Future Goals

### User Management
- [ ] User profile management (e.g., update profile, change password).
- [ ] User deactivation and deletion.

### Ticket Management
- [ ] Update ticket by ID.
- [ ] Delete ticket by ID.
- [ ] Assign ticket to a user.
- [ ] Get tickets assigned to a user.
- [ ] Add comments to tickets.

### Notifications
- [ ] Email notifications for new tickets and updates.

### Search and Filtering
- [ ] Search tickets by keyword.
- [ ] Filter tickets by status, priority, and assignee.

### Dashboard
- [ ] A dashboard for users to view their tickets.
- [ ] A dashboard for admins to view all tickets and statistics.
