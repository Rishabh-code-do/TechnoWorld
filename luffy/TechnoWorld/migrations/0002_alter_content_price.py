# Generated by Django 3.2.7 on 2021-09-10 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TechnoWorld', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='price',
            field=models.IntegerField(),
        ),
    ]
