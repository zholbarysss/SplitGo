# SplitGo — Expense Sharing REST API

SplitGo is a backend application for managing shared expenses
and calculating balances between group members.

## Technologies
- Python
- FastAPI
- Pydantic
- Git

## Features
- Create and manage groups
- Add and manage expenses
- Update expenses
- Delete groups and expenses
- Calculate balances between members
- Validate user input
- Handle API errors

## Installation

1. Clone the repository.
2. Create a virtual environment:

   python3 -m venv venv

3. Activate the environment:

   source venv/bin/activate

4. Install dependencies:

   pip install -r requirements.txt

5. Run the server:

   uvicorn main:app --reload

6. Open Swagger UI:

   http://127.0.0.1:8000/docs

## API Endpoints

### Groups
- POST /groups/
- GET /groups/
- GET /groups/{group_id}
- DELETE /groups/{group_id}

### Expenses
- POST /expenses/
- GET /expenses/
- GET /expenses/{expense_id}
- PATCH /expenses/{expense_id}
- DELETE /expenses/{expense_id}

### Balances
- GET /balances/{group_id}

## Data Storage

The application uses in-memory Python dictionaries.
Data resets when the server restarts.