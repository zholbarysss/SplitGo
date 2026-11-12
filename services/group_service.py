from fastapi import HTTPException

groups = {}
next_id = 1

def create_group(data):
    global next_id

    group = {
        "id": next_id,
        "name": data.name,
        "members": data.members
    }

    groups[next_id] = group
    next_id += 1

    return group

def get_groups():
    return list(groups.values())

def get_group(group_id):
    if group_id not in groups:
        raise HTTPException(
            status_code=404,
            detail="Group not found"
        )

    return groups[group_id]

def delete_group(group_id):
    get_group(group_id)

    from services.expense_service import expenses

    expense_ids = [
        expense_id
        for expense_id, expense in expenses.items()
        if expense["group_id"] == group_id
    ]

    for expense_id in expense_ids:
        del expenses[expense_id]

    del groups[group_id]

    return {"message": "Group and related expenses deleted successfully"}