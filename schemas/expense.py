from pydantic import BaseModel, Field, field_validator


class ExpenseCreate(BaseModel):
    group_id: int = Field(gt=0)
    title: str = Field(min_length=2, max_length=100)
    amount: float = Field(gt=0, allow_inf_nan=False)
    paid_by: str = Field(min_length=1)

    @field_validator("paid_by")
    @classmethod
    def validate_payer(cls, value):
        if not value.strip():
            raise ValueError("Payer cannot be empty")
        return value


class ExpenseUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=2, max_length=100)
    amount: float | None = Field(default=None, gt=0, allow_inf_nan=False)
    paid_by: str | None = Field(default=None, min_length=1)

    @field_validator("title", "amount", "paid_by")
    @classmethod
    def reject_null(cls, value):
        if value is None:
            raise ValueError("Field cannot be null")
        return value

    @field_validator("paid_by")
    @classmethod
    def validate_payer(cls, value):
        if value is not None and not value.strip():
            raise ValueError("Payer cannot be empty")
        return value


class ExpenseResponse(ExpenseCreate):
    id: int