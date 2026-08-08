from fastapi import APIRouter, Depends, HTTPException 
from sqlalchemy.orm import Session 
from typing import List 
from app.core.database import get_db 
from app.models.beneficiary import Beneficiary 
from app.schemas.beneficiary import BeneficiaryCreate, BeneficiaryResponse 
import uuid 
 
router = APIRouter(prefix="/beneficiaries", tags=["Beneficiaries"]) 
 
@router.get("/", response_model=List[BeneficiaryResponse]) 
def get_beneficiaries(db: Session = Depends(get_db)): 
    return db.query(Beneficiary).filter(Beneficiary.is_active == True).all() 
 
@router.post("/", response_model=BeneficiaryResponse, status_code=201) 
def create_beneficiary(beneficiary: BeneficiaryCreate, db: Session = Depends(get_db)): 
    db_beneficiary = Beneficiary(**beneficiary.model_dump()) 
    db.add(db_beneficiary) 
    db.commit() 
    db.refresh(db_beneficiary) 
    return db_beneficiary 
 
@router.get("/{beneficiary_id}", response_model=BeneficiaryResponse) 
def get_beneficiary(beneficiary_id: str, db: Session = Depends(get_db)): 
    beneficiary = db.query(Beneficiary).filter(Beneficiary.beneficiary_id == beneficiary_id).first() 
    if not beneficiary: 
        raise HTTPException(status_code=404, detail="Beneficiary not found") 
    return beneficiary 
