from fastapi import FastAPI
from routers import groups, expenses, balances

app = FastAPI(
    title="SplitGo API",
    description="Expense sharing application",
    version="1.0.0"
)

app.include_router(groups.router)
app.include_router(expenses.router)
app.include_router(balances.router)


@app.get("/")
def home():
    return {"message": "Welcome to SplitGo API!"}