# Generated by Django 4.0.4 on 2022-05-24 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_articles_img_anons'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='img_content',
            field=models.TextField(),
        ),
    ]
