# Generated by Django 4.0.4 on 2022-05-23 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_articles_img_anons_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='img_anons',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='articles',
            name='img_content',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
