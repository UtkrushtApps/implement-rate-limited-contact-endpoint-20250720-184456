from fastapi import APIRouter
from app.models import Employee, Employees

router = APIRouter()

fake_employees = [
    Employee(id=1, name="Alice Smith", department="Engineering"),
    Employee(id=2, name="Bob Jones", department="HR"),
]

@router.get("/employees", response_model=Employees)
def get_employees():
    return Employees(employees=fake_employees)
