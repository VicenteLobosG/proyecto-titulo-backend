from django.db.models import Model, IntegerField, ForeignKey, CASCADE
from control_productos.models import Product

class PurchaseOrder(Model):
    sale = ForeignKey('Sale', on_delete=CASCADE)
    product = ForeignKey(Product, on_delete=CASCADE)
    quantity = IntegerField()
    total = IntegerField()

    def __str__(self):
        return f'Purchase Order {self.id}'
