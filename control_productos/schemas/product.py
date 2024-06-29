from ninja import Schema
from pydantic import field_validator

from control_productos.models import Category
from proyecto_titulo_backend.error_handler import FKDoesntExist

class ProductCreateUpdateSchema(Schema):
    name: str
    price: int
    category: int

    @field_validator('category')
    def validate_category_id(cls, value):
        if not Category.objects.filter(id=value).exists():
            raise FKDoesntExist('Category', 'id', value)
        
        return value

