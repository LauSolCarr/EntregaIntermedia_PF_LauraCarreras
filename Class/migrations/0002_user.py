# Generated by Django 4.0.3 on 2022-03-20 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Class', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('tipo', models.CharField(max_length=10)),
            ],
        ),
    ]
