from fastapi import APIRouter, status
from schemas.group import GroupCreate, GroupResponse
from services import group_service

router = APIRouter(prefix="/groups", tags=["Groups"])

@router.post(
    "/",
    response_model=GroupResponse,
    status_code=status.HTTP_201_CREATED
)
def create_group(data: GroupCreate):
    return group_service.create_group(data)

@router.get("/", response_model=list[GroupResponse])
def get_groups():
    return group_service.get_groups()

@router.get("/{group_id}", response_model=GroupResponse)
def get_group(group_id: int):
    return group_service.get_group(group_id)

@router.delete("/{group_id}")
def delete_group(group_id: int):
    return group_service.delete_group(group_id)