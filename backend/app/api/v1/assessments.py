from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db
from app.models.assessment import Assessment
from app.schemas.assessment import AssessmentCreate, AssessmentResponse

router = APIRouter(prefix="/assessments", tags=["Assessments"])

@router.get("/", response_model=List[AssessmentResponse])
def get_assessments(db: Session = Depends(get_db)):
    return db.query(Assessment).all()

@router.post("/", response_model=AssessmentResponse, status_code=201)
def create_assessment(assessment: AssessmentCreate, db: Session = Depends(get_db)):
    percentage = (assessment.obtained_score / assessment.total_score) * 100

    if percentage >= 90:
        grade = "A"
    elif percentage >= 80:
        grade = "B"
    elif percentage >= 70:
        grade = "C"
    elif percentage >= 60:
        grade = "D"
    else:
        grade = "F"

    db_assessment = Assessment(**assessment.model_dump(), percentage=percentage, grade=grade)
    db.add(db_assessment)
    db.commit()
    db.refresh(db_assessment)
    return db_assessment

@router.get("/{assessment_id}", response_model=AssessmentResponse)
def get_assessment(assessment_id: str, db: Session = Depends(get_db)):
    assessment = db.query(Assessment).filter(Assessment.id == assessment_id).first()
    if not assessment:
        raise HTTPException(status_code=404, detail="Assessment not found")
    return assessment

@router.get("/beneficiary/{beneficiary_id}", response_model=List[AssessmentResponse])
def get_assessments_by_beneficiary(beneficiary_id: str, db: Session = Depends(get_db)):
    return db.query(Assessment).filter(Assessment.beneficiary_id == beneficiary_id).all()

@router.get("/program/{program_id}", response_model=List[AssessmentResponse])
def get_assessments_by_program(program_id: str, db: Session = Depends(get_db)):
    return db.query(Assessment).filter(Assessment.program_id == program_id).all()
