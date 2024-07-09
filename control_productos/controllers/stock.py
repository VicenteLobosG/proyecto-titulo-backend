from ninja_extra import api_controller, ModelControllerBase, ModelConfig, ModelSchemaConfig, ModelService

from control_productos.models import Stock
from control_productos.schemas import StockCreateUpdateSchema
    

@api_controller('/stocks')
class StockController(ModelControllerBase):
    service = ModelService(model=Stock)
    model_config = ModelConfig(
        allowed_routes=['list', 'find_one', 'create', 'update', 'delete'],
        model=Stock,
        schema_config=ModelSchemaConfig(read_only_fields=['id', 'update_date']),
        create_schema=StockCreateUpdateSchema,
        update_schema=StockCreateUpdateSchema,
        #retrieve_schema=
    )
    