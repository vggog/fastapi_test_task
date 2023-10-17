from datetime import datetime

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    ...


class QuizQuestion(Base):
    __tablename__ = "quiz_questions"

    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[datetime] = mapped_column(
        default=datetime.utcnow()
    )

    question: Mapped[str]
    answer: Mapped[str]

    def __repr__(self):
        return (
            f"{self.id}\n"
            f"{self.question}\n"
            "\n"
            f"Ответ: {self.answer}"
        )
