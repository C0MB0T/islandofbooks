# Generated by Django 2.1.4 on 2019-05-02 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(max_length=99),
        ),
    ]
