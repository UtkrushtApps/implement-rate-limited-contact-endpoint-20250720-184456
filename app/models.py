from pydantic import BaseModel
from typing import List

class Employee(BaseModel):
    id: int
    name: str
    department: str

class Employees(BaseModel):
    employees: List[Employee]