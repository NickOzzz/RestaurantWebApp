# Generated by Django 3.0.1 on 2022-11-08 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wannaShashApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='Price',
            field=models.IntegerField(),
        ),
    ]
