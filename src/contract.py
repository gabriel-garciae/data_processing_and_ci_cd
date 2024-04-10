from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt, field_validator
from datetime import datetime
from enum import Enum


#If Pydantic's imports don't work for you, you can create your own, like below
class CategoryEnum(str, Enum):
    category1 = "category1"
    category2 = "category2"
    category3 = "category3"


class Vendas(BaseModel):
    email: EmailStr
    date: datetime
    value: PositiveFloat
    product: str
    amount: PositiveInt
    category: CategoryEnum

    @field_validator('category')
    def category_should_be_in_enum(cls, error):
        return error