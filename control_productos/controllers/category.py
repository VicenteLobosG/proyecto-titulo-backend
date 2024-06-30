from ninja_extra import api_controller, ModelControllerBase, ModelConfig, ModelSchemaConfig, ModelService

from control_productos.models import Category

@api_controller('/category')
class CategoryController(ModelControllerBase):
    service = ModelService(model=Category)
    model_config = ModelConfig(
        model=Category,
        allowed_routes=['list', 'find_one', 'create', 'update', 'delete'],
        schema_config=ModelSchemaConfig(read_only_fields=['id']),
    )
    