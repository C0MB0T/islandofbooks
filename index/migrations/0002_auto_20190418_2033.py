# Generated by Django 2.1.4 on 2019-04-18 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authors',
            name='img',
            field=models.ImageField(upload_to='index/static/image/foto'),
        ),
    ]
