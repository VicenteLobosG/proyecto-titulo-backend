from django.db.models import Model, CharField, IntegerField, ForeignKey, CASCADE

class Product(Model):
    name = CharField(max_length=100)
    price = IntegerField()
    category = ForeignKey('Category', on_delete=CASCADE)
