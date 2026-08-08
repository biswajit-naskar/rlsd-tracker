from fastapi import APIRouter, Depends, HTTPException 
from sqlalchemy.orm import Session 
from typing import List 
from uuid import UUID 
from app.core.database import get_db 
from app.models.employment import Employment 
from app.schemas.employment import EmploymentCreate, EmploymentResponse 
 
router = APIRouter(prefix="/employment", tags=["Employment"]) 
 
@router.get("/", response_model=List[EmploymentResponse]) 
def get_all_employment(db: Session = Depends(get_db)): 
    return db.query(Employment).all() 
 
@router.post("/", response_model=EmploymentResponse, status_code=201) 
def create_employment(employment: EmploymentCreate, db: Session = Depends(get_db)): 
    db_employment = Employment(**employment.model_dump()) 
    db.add(db_employment) 
    db.commit() 
    db.refresh(db_employment) 
    return db_employment 
 
@router.get("/{employment_id}", response_model=EmploymentResponse) 
def get_employment(employment_id: str, db: Session = Depends(get_db)): 
    try: 
        uuid_obj = UUID(employment_id) 
    except ValueError: 
        raise HTTPException(status_code=400, detail="Invalid UUID format") 
 
    employment = db.query(Employment).filter(Employment.id == uuid_obj).first() 
    if not employment: 
        raise HTTPException(status_code=404, detail="Employment record not found") 
    return employment 
 
@router.get("/beneficiary/{beneficiary_id}", response_model=List[EmploymentResponse]) 
def get_employment_by_beneficiary(beneficiary_id: str, db: Session = Depends(get_db)): 
    try: 
        uuid_obj = UUID(beneficiary_id) 
    except ValueError: 
        raise HTTPException(status_code=400, detail="Invalid UUID format") 
 
    return db.query(Employment).filter(Employment.beneficiary_id == uuid_obj).all() 
 
@router.get("/program/{program_id}", response_model=List[EmploymentResponse]) 
def get_employment_by_program(program_id: str, db: Session = Depends(get_db)): 
    try: 
        uuid_obj = UUID(program_id) 
    except ValueError: 
        raise HTTPException(status_code=400, detail="Invalid UUID format") 
 
    return db.query(Employment).filter(Employment.program_id == uuid_obj).all() 
