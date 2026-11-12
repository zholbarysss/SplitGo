from fastapi import APIRouter
from services.balance_service import calculate_balances

router = APIRouter(
    prefix="/balances",
    tags=["Balances"]
)


@router.get("/{group_id}")
def get_balances(group_id: int):
    return calculate_balances(group_id)