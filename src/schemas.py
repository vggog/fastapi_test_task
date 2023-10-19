from datetime import datetime

from pydantic import BaseModel


class QuestionsNumSchema(BaseModel):
    questions_num: int


class QuestionSchema(BaseModel):
    id: int
    created_at: datetime
    question: str
    answer: str
