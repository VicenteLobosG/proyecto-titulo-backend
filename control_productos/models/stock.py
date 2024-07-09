from django.db.models import Model, DateTimeField, ForeignKey, CASCADE, IntegerField

class Stock(Model):
    product = ForeignKey('Product', on_delete=CASCADE)
    quantity = IntegerField()
    update_date = DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.product.name}: {self.quantity}'
    