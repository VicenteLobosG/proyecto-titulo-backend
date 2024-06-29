from ninja.errors import ValidationError

class FKDoesntExist(ValidationError):
    def __init__(self, model, field, value):
        self.model = model
        self.field = field
        self.value = value
        super().__init__(f'{model} with {field}={value} does not exist')
