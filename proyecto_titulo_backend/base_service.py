from pydantic import BaseModel as PydanticModel
from ninja_extra import ModelService

class BaseModelService(ModelService):
    def __init__(self, model, custom_schema: PydanticModel=None):
        super().__init__(model)
        self.custom_schema = custom_schema
    
    def create(self, schema: PydanticModel, **kwargs):
        if self.custom_schema:
            validated_schema = self.custom_schema(**schema.dict())
        else:
            validated_schema = schema

        data = validated_schema.model_dump(by_alias=True)
        data.update(kwargs)

        instance = self.model._default_manager.create(**data)
        return instance
