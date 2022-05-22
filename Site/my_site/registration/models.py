from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)
    mail = models.EmailField(max_length=75)
    date_join = models.DateTimeField('Дата регистрации',blank=True)

# Create your models here.
