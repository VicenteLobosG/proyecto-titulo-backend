from django.db.models import Model, IntegerField, ForeignKey, CASCADE, DateTimeField

class Sale(Model):
    user = ForeignKey('User', on_delete=CASCADE)
    date_sale = DateTimeField(auto_now_add=True)
    total = IntegerField()
    ticket = IntegerField()

    def __str__(self):
        return f'Sale {self.id}'
    