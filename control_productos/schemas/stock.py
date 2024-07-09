from ninja import Schema
from datetime import datetime
from pydantic import field_validator

from control_productos.models import Product
from proyecto_titulo_backend.error_handler import FKDoesntExist

class StockCreateUpdateSchema(Schema):
    product_id: int
    quantity: int
    update_date: datetime

    @field_validator('product_id')
    def validate_product_id(cls, value):
        if not Product.objects.filter(id=value).exists():
            raise FKDoesntExist('Product', 'id', value)
        
        return value
    
    @property
    def formatted_update_date(self):
        return self.update_date.strftime('%Y-%m-%d %H:%M:%S')
    

class StockSchema(Schema):
    product_id: int
    quantity: int
    update_date: datetime
