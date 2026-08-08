from fastapi import APIRouter, Depends, HTTPException 
from sqlalchemy.orm import Session 
from typing import List 
from app.core.database import get_db 
from app.models.program import TrainingProgram 
from app.schemas.program import ProgramCreate, ProgramResponse 
 
router = APIRouter(prefix="/programs", tags=["Programs"]) 
 
@router.get("/", response_model=List[ProgramResponse]) 
def get_programs(db: Session = Depends(get_db)): 
    return db.query(TrainingProgram).all() 
 
@router.post("/", response_model=ProgramResponse, status_code=201) 
def create_program(program: ProgramCreate, db: Session = Depends(get_db)): 
    db_program = TrainingProgram(**program.model_dump()) 
    db.add(db_program) 
    db.commit() 
    db.refresh(db_program) 
    return db_program 
 
@router.get("/{program_code}", response_model=ProgramResponse) 
def get_program(program_code: str, db: Session = Depends(get_db)): 
    program = db.query(TrainingProgram).filter(TrainingProgram.program_code == program_code).first() 
    if not program: 
        raise HTTPException(status_code=404, detail="Program not found") 
    return program 
