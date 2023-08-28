# Импортируем модуль requests для выполнения HTTP-запросов
import requests
# Импортируем константу SERVICE_URL из модуля config
from config import SERVICE_URL
# Импортируем перечисление GlobalErrorMessage из модуля global_enums
from src.enums.global_enums import GlobalErrorMessage
from src.baseclasses.response import Response
# Импортируем JSON Schema для валидации данных
#from src.schemas.post import POST_SCHEMA
from src.pydantic_schema.post import Post

# Тест для получения данных о компаниях
def test_getting_posts():
    # Отправляем GET-запрос на SERVICE_URL
    r = requests.get(url=SERVICE_URL)
    response = Response(r)

    response.assert_status_code(200).validate(Post)
    #response.assert_status_code(200).validate(POST_SCHEMA)
