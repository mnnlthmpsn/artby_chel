# Generated by Django 3.0.7 on 2020-07-27 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_auto_20200713_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='image',
            field=models.FileField(upload_to='documents/'),
        ),
    ]