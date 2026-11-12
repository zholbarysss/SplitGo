from fastapi import HTTPException
from services.group_service import get_group

expenses = {}
next_id = 1

def create_expense(data):
    global next_id

    group = get_group(data.group_id)

    if data.paid_by not in group["members"]:
        raise HTTPException(
            status_code=400,
            detail="Payer must be a group member"
        )

    expense = {
        "id": next_id,
        "group_id": data.group_id,
        "title": data.title,
        "amount": data.amount,
        "paid_by": data.paid_by
    }

    expenses[next_id] = expense
    next_id += 1

    return expense

def get_expenses(group_id=None):
    if group_id is not None:
        get_group(group_id)
        return [
            expense for expense in expenses.values()
            if expense["group_id"] == group_id
        ]

    return list(expenses.values())

def get_expense(expense_id):
    if expense_id not in expenses:
        raise HTTPException(
            status_code=404,
            detail="Expense not found"
        )

    return expenses[expense_id]

def delete_expense(expense_id):
    get_expense(expense_id)
    del expenses[expense_id]

    return {"message": "Expense deleted successfully"}
def update_expense(expense_id, data):
    expense = get_expense(expense_id)

    updates = data.model_dump(exclude_unset=True)

    if "paid_by" in updates:
        group = get_group(expense["group_id"])

        if updates["paid_by"] not in group["members"]:
            raise HTTPException(
                status_code=400,
                detail="Payer must be a group member"
            )

    expense.update(updates)

    return expense