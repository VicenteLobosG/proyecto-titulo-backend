from ninja_extra import api_controller, ModelControllerBase, ModelConfig, ModelSchemaConfig

from control_productos.models import Product
from control_productos.schemas.product import ProductCreateUpdateSchema
from proyecto_titulo_backend.base_service import BaseModelService

@api_controller('/products')
class ProductController(ModelControllerBase):
    service = BaseModelService(model=Product, custom_schema=ProductCreateUpdateSchema)
    model_config = ModelConfig(
        model=Product,
        schema_config=ModelSchemaConfig(read_only_fields=['id']),
    )
