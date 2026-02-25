# models.py
import uuid
from sqlalchemy import Column, String, Text, DateTime
from sqlalchemy.sql import func
from database import Base

class AnalysisResult(Base):
    __tablename__ = "analysis_results"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    filename = Column(String, nullable=False)
    query = Column(Text, nullable=False)
    result = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())