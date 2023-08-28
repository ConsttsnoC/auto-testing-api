# Импортируем функцию validate из модуля jsonschema для валидации данных
#from jsonschema import validate

# Импортируем перечисление GlobalErrorMessage из модуля global_enums
from src.enums.global_enums import GlobalErrorMessage

# Определяем класс Response для обработки HTTP-ответов
class Response:

    # Конструктор класса, принимает объект response в качестве аргумента
    def __init__(self, response):
        # Сохраняем переданный объект response как атрибут объекта
        self.response = response
        # Получаем JSON-представление ответа и сохраняем как атрибут объекта
        self.response_json = response.json().get('data')
        # Получаем статусный код ответа и сохраняем как атрибут объекта
        self.response_status = response.status_code

    # Метод для валидации ответа по заданной JSON-схеме
    def validate(self, schema):
        # Проверяем, является ли JSON ответа списком
        if isinstance(self.response_json, list):
            # Если да, проходим по элементам списка и валидируем каждый по схеме
            for item in self.response_json:
                schema.model_validate(item)
                #validate(item, schema)
        else:
            schema.model_validate(self.response_json)
            # Если нет, валидируем весь JSON ответа по схеме
            #validate(self.response.json, schema)


    # Метод для проверки статусного кода ответа
    def assert_status_code(self, status_code):
        # Проверяем, является ли переданный статусный код списком
        if isinstance(status_code, list):
            # Если да, проверяем, что текущий статусный код находится в списке
            assert self.response_status in status_code, GlobalErrorMessage.WRONG_STATUS_CODE.value
        else:
            # Если нет, проверяем, что текущий статусный код совпадает с переданным
            assert self.response_status == status_code, GlobalErrorMessage.WRONG_STATUS_CODE.value
        return self  # Возвращаем объект класса Response для поддержки цепочек вызовов
