from ninja_extra import api_controller, ModelControllerBase, ModelConfig, ModelSchemaConfig, ModelService

from control_productos.models import Product
from control_productos.schemas import ProductCreateUpdateSchema
    

@api_controller('/products')
class ProductController(ModelControllerBase):
    service = ModelService(model=Product)
    model_config = ModelConfig(
        allowed_routes=['list', 'find_one', 'create', 'update', 'delete'],
        model=Product,
        schema_config=ModelSchemaConfig(read_only_fields=['id']),
        create_schema=ProductCreateUpdateSchema,
        update_schema=ProductCreateUpdateSchema,
    )
