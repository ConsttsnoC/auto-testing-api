#Enum (перечисление) - это концепция, используемая в программировании для определения типа данных,
# который может принимать только определенные значения, перечисленные заранее.
# В языке программирования Python модуль enum предоставляет специальный класс Enum,
# который позволяет создавать перечисления.
from enum import Enum

class GlobalErrorMessage(Enum):
    WRONG_STATUS_CODE = "Неверный статус код"