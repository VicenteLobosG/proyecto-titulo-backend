from pydantic import BaseModel as PydanticModel
from ninja_extra import ModelService

class BaseModelService(ModelService):
    def __init__(self, model, fk_validation_schema: PydanticModel):
        super().__init__(model)
        self.fk_validation_schema = fk_validation_schema
    
    def create(self, schema: PydanticModel, **kwargs):
        validated_schema = self.fk_validation_schema(**schema.dict())
        data = validated_schema.model_dump(by_alias=True)
        data.update(kwargs)

        instance = self.model._default_manager.create(**data)
        return instance
    
    def update(self, instance, schema: PydanticModel, **kwargs):
        validated_schema = self.fk_validation_schema(**schema.dict())
        data = validated_schema.model_dump(exclude_none=True)
        data.update(kwargs)
        for attr, value in data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
