import requests

from src.config import project_config
from src.repository import Repository
from src.model import QuizQuestion
from src.schemas import QuestionSchema


class Service:
    questions_api_url = project_config.url_for_questions
    repository = Repository()

    def add_questions(self, count: int):
        """
        Сохраняет полученные вопросы викторины. Если вопрос уже существует
        в бд, то делает новые запросы, пока не будет добавлено нужное
        количество вопросов.
        :param count: Количество вопросов.
        :return:
        """
        while count > 0:
            questions = self.get_questions(count)

            for question in questions:
                if self.repository.get_question(question_id=question["id"]):
                    continue

                quiz_question = Service.create_quiz_question_model(question)

                self.repository.add_question(quiz_question)

                count -= 1

    def get_questions(self, count: int) -> dict:
        """
        Делает запрос на сторонний api для получения вопросов.
        Полученный ответ конвертирует в python-словарь.
        :param count: Количество вопросов.
        :return:
        """
        response = requests.get(self.questions_api_url.format(count))
        return response.json()

    def get_previous_question(self) -> QuestionSchema | None:
        """
        Метод для полученияя предыдущего сохранённого вопроса.
        :return:
        """
        last_quiz_question = self.repository.get_last_added_question()

        if last_quiz_question is None:
            return None

        return QuestionSchema(
            id=last_quiz_question.id,
            created_at=last_quiz_question.created_at,
            question=last_quiz_question.question,
            answer=last_quiz_question.answer
        )

    @staticmethod
    def create_quiz_question_model(question: dict) -> QuizQuestion:
        """
        Создание модели вопроса для сохранения в бд.
        :param question: Словарь, обладающий ключами <question> и <answer>
        :return:
        """
        try:
            return QuizQuestion(
                question=question["question"],
                answer=question["answer"],
            )
        except KeyError as e:
            print("----------Ошибка----------")
            print(e)
            print(question)
            print("--------------------------")
