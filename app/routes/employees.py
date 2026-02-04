from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.models.database import get_db
from app.models.employee import Employee as EmployeeModel
from app.schemas.employee import Employee

router = APIRouter()


@router.get("/employees/list", response_model=List[Employee])
async def list_employees(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    """Liste tous les employés avec pagination."""
    employees = db.query(EmployeeModel).offset(skip).limit(limit).all()
    return employees
