from django.db import models

# Create your models here.

class Articles(models.Model):
    name = models.CharField('Название',max_length=30)
    anons = models.CharField('Анонс',max_length=200)
    content = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации',blank=True)
    meta = models.CharField(max_length=30)

    def __str__(self):
        return self.name

