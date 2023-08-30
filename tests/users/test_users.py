# Импортируем модуль requests для выполнения HTTP-запросов
# Импортируем константу SERVICE_URL из модуля config
# Импортируем перечисление GlobalErrorMessage из модуля global_enums
from src.baseclasses.response import Response
# Импортируем JSON Schema для валидации данных
#from src.schemas.post import POST_SCHEMA
from src.schemas.user import User


# Тест для получения данных о компаниях
# def test_getting_posts():
#     # Отправляем GET-запрос на SERVICE_URL
#     r = requests.get(url=SERVICE_URL)
#     response = Response(r)
#     response.assert_status_code(200).validate(Post)
    #response.assert_status_code(200).validate(POST_SCHEMA)


def test_getting_user_list(get_users, get_number):
    Response(get_users).assert_status_code(200).validate(User)
    print(get_number)

