from ninja_extra import NinjaExtraAPI
from ninja import Swagger

from control_productos.controllers import ProductController, CategoryController, StockController
from proyecto_titulo_backend.error_handler import FKDoesntExist

api = NinjaExtraAPI(docs=Swagger(settings={}))
api.register_controllers(ProductController)
api.register_controllers(CategoryController)
api.register_controllers(StockController)

@api.exception_handler(FKDoesntExist)
def fk_doesnt_exist(request, exc):
    return api.create_response(request, {'detail': str(exc)}, status=404)
