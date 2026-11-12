from fastapi import APIRouter, status
from schemas.expense import ExpenseCreate, ExpenseUpdate, ExpenseResponse
from services import expense_service

router = APIRouter(prefix="/expenses", tags=["Expenses"])

@router.post(
    "/",
    response_model=ExpenseResponse,
    status_code=status.HTTP_201_CREATED
)
def create_expense(data: ExpenseCreate):
    return expense_service.create_expense(data)

@router.get("/", response_model=list[ExpenseResponse])
def get_expenses(group_id: int | None = None):
    return expense_service.get_expenses(group_id)

@router.get("/{expense_id}", response_model=ExpenseResponse)
def get_expense(expense_id: int):
    return expense_service.get_expense(expense_id)

@router.delete("/{expense_id}")
def delete_expense(expense_id: int):
    return expense_service.delete_expense(expense_id)
@router.patch("/{expense_id}", response_model=ExpenseResponse)
def update_expense(expense_id: int, data: ExpenseUpdate):
    return expense_service.update_expense(expense_id, data)