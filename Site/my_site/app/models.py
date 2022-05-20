from django.db import models

# Create your models here.
class Articles(models.Model):
    name = models.CharField(max_length=30)
    content = models.CharField(max_length=300)
    date = models.DateField

class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return f'id({self.id}) {self.title}'

    class Meta:
        ordering = ('id', 'title')


class User(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(blank=True)
    about = models.TextField()
    category = models.ManyToManyField(Category)

    class Meta:
        ordering = ('id', 'name')