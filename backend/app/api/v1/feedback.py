from fastapi import APIRouter, Depends, HTTPException 
from sqlalchemy.orm import Session 
from typing import List 
from app.core.database import get_db 
from app.models.feedback import Feedback 
from app.schemas.feedback import FeedbackCreate, FeedbackResponse 
 
router = APIRouter(prefix="/feedback", tags=["Feedback"]) 
 
@router.get("/", response_model=List[FeedbackResponse]) 
def get_all_feedback(db: Session = Depends(get_db)): 
    return db.query(Feedback).all() 
 
@router.post("/", response_model=FeedbackResponse, status_code=201) 
def create_feedback(feedback: FeedbackCreate, db: Session = Depends(get_db)): 
    db_feedback = Feedback(**feedback.model_dump()) 
    db.add(db_feedback) 
    db.commit() 
    db.refresh(db_feedback) 
    return db_feedback 
 
@router.get("/{feedback_id}", response_model=FeedbackResponse) 
def get_feedback(feedback_id: str, db: Session = Depends(get_db)): 
    feedback = db.query(Feedback).filter(Feedback.id == feedback_id).first() 
    if not feedback: 
        raise HTTPException(status_code=404, detail="Feedback not found") 
    return feedback 
 
@router.get("/beneficiary/{beneficiary_id}", response_model=List[FeedbackResponse]) 
def get_feedback_by_beneficiary(beneficiary_id: str, db: Session = Depends(get_db)): 
    return db.query(Feedback).filter(Feedback.beneficiary_id == beneficiary_id).all() 
 
@router.get("/program/{program_id}", response_model=List[FeedbackResponse]) 
def get_feedback_by_program(program_id: str, db: Session = Depends(get_db)): 
    return db.query(Feedback).filter(Feedback.program_id == program_id).all() 
@router.get("/analytics/summary") 
def get_feedback_analytics(db: Session = Depends(get_db)): 
    feedbacks = db.query(Feedback).all() 
    if not feedbacks: 
        return {"message": "No feedback data available"} 
 
    total = len(feedbacks) 
    avg_satisfaction = sum(f.satisfaction_score for f in feedbacks) / total 
    avg_quality = sum(f.training_quality for f in feedbacks) / total 
    follow_up_count = sum(1 for f in feedbacks if f.follow_up_required) 
 
    return { 
        "total_feedback": total, 
        "average_satisfaction": round(avg_satisfaction, 2), 
        "average_training_quality": round(avg_quality, 2), 
        "follow_up_required": follow_up_count, 
        "follow_up_percentage": round((follow_up_count / total) * 100, 2) 
    } 
