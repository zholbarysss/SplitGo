from services.group_service import get_group
from services.expense_service import get_expenses


def calculate_balances(group_id):
    group = get_group(group_id)
    members = group["members"]

    balances = {member: 0.0 for member in members}

    expenses = get_expenses(group_id)

    for expense in expenses:
        amount = expense["amount"]
        paid_by = expense["paid_by"]

        share = amount / len(members)

        balances[paid_by] += amount

        for member in members:
            balances[member] -= share

    return {
        "group_id": group_id,
        "balances": {
            member: round(balance, 2)
            for member, balance in balances.items()
        }
    }