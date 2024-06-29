from django.db.models import Model, BooleanField, ForeignKey, CASCADE, IntegerField

class Alert(Model):
    product = ForeignKey('Product', on_delete=CASCADE)
    active = BooleanField(default=False)
    stock = IntegerField(default=10)
    
    def __str__(self):
        return f'{self.product.name}: {self.stock} - {self.active}'