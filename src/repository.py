from sqlalchemy import create_engine, func, select, insert
from sqlalchemy.orm import Session

from src.config import db_config
from src.model import QuizQuestion


class Repository:
    engine = create_engine(db_config.alchemy_url)

    def get_question(self, question_id: int) -> QuizQuestion | None:
        with Session(self.engine) as session:
            stmt = select(QuizQuestion).where(QuizQuestion.id == question_id)
            return session.scalars(stmt).first()

    def add_question(self, question: QuizQuestion):
        with Session(self.engine) as session:
            session.add(question)
            session.commit()

    def get_last_added_question(self) -> QuizQuestion | None:
        with Session(self.engine) as session:
            last_id = session.execute(func.max(QuizQuestion.id)).first()[0]
            stmt = select(QuizQuestion).where(QuizQuestion.id == last_id)

            return session.scalars(stmt).first()
