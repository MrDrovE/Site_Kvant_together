# Generated by Django 4.0.4 on 2022-05-24 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_articles_img_anons_alter_articles_img_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='img_anons',
            field=models.TextField(),
        ),
    ]
