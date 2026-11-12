from pydantic import BaseModel, Field, field_validator


class GroupCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    members: list[str] = Field(min_length=2)

    @field_validator("members")
    @classmethod
    def validate_members(cls, members):
        if any(not member.strip() for member in members):
            raise ValueError("Member names cannot be empty")

        if len(members) != len(set(members)):
            raise ValueError("Duplicate members are not allowed")

        return members


class GroupResponse(BaseModel):
    id: int
    name: str
    members: list[str]