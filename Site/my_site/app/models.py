from django.db import models

from django.contrib.auth.models import User
#from registration.models import User
# Create your models here.

class Articles(models.Model):
    name = models.CharField('Название',max_length=30)
    anons = models.CharField('Анонс',max_length=200)
    img_anons = models.TextField()
    content = models.TextField('Статья')
    img_content = models.TextField()
    date = models.DateTimeField('Дата публикации',blank=True)
    meta = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Comments(models.Model):
    author_id = models.ForeignKey(User,on_delete= models.CASCADE,verbose_name='Автор коментария',
                                  blank=True,null=True)
    post_id = models.ForeignKey(Articles,on_delete= models.CASCADE,related_name='comments_articles')
    create_date = models.DateTimeField(auto_now=True)
    content = models.TextField(verbose_name='Текст коментария')
