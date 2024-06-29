from django.db.models import CharField, IntegerField, ForeignKey, CASCADE, ManyToManyField
from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):
    name = CharField(max_length=100)
    email = CharField(max_length=100)
    position = CharField(max_length=100)
    address = CharField(max_length=100)

    groups = ManyToManyField(Group, related_name='registro_ventas_user_groups', blank=True)
    user_permissions = ManyToManyField(Permission, related_name='registro_ventas_user_permissions', blank=True)
    
    def __str__(self):
        return f'{self.name}'
    