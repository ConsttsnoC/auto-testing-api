from pydantic import BaseModel, field_validator
from src.enums.user_enums import Genders, Statuses, UserErrors

class User(BaseModel):
    id: int
    name: str
    email: str
    gender: Genders
    status: Statuses

