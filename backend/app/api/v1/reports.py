from fastapi import APIRouter, Depends, HTTPException 
from fastapi.responses import FileResponse 
from sqlalchemy.orm import Session 
from app.core.database import get_db 
from app.models.beneficiary import Beneficiary 
from app.services.reports.pdf_generator import generate_beneficiary_report 
from app.services.reports.excel_generator import generate_beneficiary_excel 
from datetime import datetime 
import os 
 
router = APIRouter(prefix="/reports", tags=["Reports"]) 
 
@router.get("/beneficiaries/pdf") 
def export_beneficiaries_pdf(db: Session = Depends(get_db)): 
    beneficiaries = db.query(Beneficiary).all() 
    if not beneficiaries: 
        raise HTTPException(status_code=404, detail="No beneficiaries found") 
 
    data = [] 
    for b in beneficiaries: 
        data.append({ 
            "beneficiary_id": b.beneficiary_id, 
            "full_name": b.full_name, 
            "gender": b.gender, 
            "village": b.village, 
            "block": b.block, 
            "district": b.district, 
            "family_income": b.family_income 
        }) 
 
    filename = generate_beneficiary_report(data) 
    return FileResponse(filename, media_type="application/pdf", filename=os.path.basename(filename)) 
 
@router.get("/beneficiaries/excel") 
def export_beneficiaries_excel(db: Session = Depends(get_db)): 
    beneficiaries = db.query(Beneficiary).all() 
    if not beneficiaries: 
        raise HTTPException(status_code=404, detail="No beneficiaries found") 
 
    data = [] 
    for b in beneficiaries: 
        data.append({ 
            "beneficiary_id": b.beneficiary_id, 
            "full_name": b.full_name, 
            "date_of_birth": b.date_of_birth, 
            "gender": b.gender, 
            "contact_number": b.contact_number, 
            "email": b.email, 
            "village": b.village, 
            "block": b.block, 
            "district": b.district, 
            "education_level": b.education_level, 
            "occupation": b.occupation, 
            "family_income": b.family_income 
        }) 
 
    filename = generate_beneficiary_excel(data) 
    return FileResponse(filename, media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", filename=os.path.basename(filename)) 
