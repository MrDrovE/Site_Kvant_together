# Generated by Django 4.0.4 on 2022-05-23 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_delete_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='img_anons',
            field=models.CharField(default=12, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='articles',
            name='img_content',
            field=models.CharField(default=12, max_length=100),
            preserve_default=False,
        ),
    ]
