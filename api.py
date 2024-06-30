from ninja_extra import NinjaExtraAPI
from ninja import Swagger

from control_productos.controllers import ProductController, CategoryController
from proyecto_titulo_backend.error_handler import FKDoesntExist

api = NinjaExtraAPI(docs=Swagger(settings={}))
api.register_controllers(ProductController)
api.register_controllers(CategoryController)

@api.exception_handler(FKDoesntExist)
def fk_doesnt_exist(request, exc):
    return api.create_response(request, {'detail': str(exc)}, status=404)
