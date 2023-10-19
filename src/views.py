from fastapi import APIRouter, Depends

from src.schemas import QuestionsNumSchema, QuestionSchema
from src.service import Service


router = APIRouter(prefix="/api")


@router.post(
    "/questions",
    response_model=QuestionSchema | None,
)
def get_questions(
        data: QuestionsNumSchema,
        service=Depends(Service),
):
    previous_question = service.get_previous_question()
    service.add_questions(data.questions_num)

    return previous_question
