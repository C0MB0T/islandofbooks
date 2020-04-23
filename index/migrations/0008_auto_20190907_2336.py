# Generated by Django 2.2.4 on 2019-09-07 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0007_auto_20190510_2239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authors',
            name='address',
        ),
        migrations.RemoveField(
            model_name='book',
            name='address',
        ),
        migrations.RemoveField(
            model_name='book',
            name='links',
        ),
        migrations.RemoveField(
            model_name='genre',
            name='address',
        ),
        migrations.AlterField(
            model_name='authors',
            name='biography',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='authors',
            name='img',
            field=models.ImageField(blank=True, upload_to='foto/'),
        ),
        migrations.AlterField(
            model_name='authors',
            name='name',
            field=models.CharField(db_index=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(db_index=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='genre',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.CreateModel(
            name='BookFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_file', models.FileField(upload_to='books/')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.Book')),
            ],
        ),
    ]