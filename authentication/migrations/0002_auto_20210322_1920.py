# Generated by Django 3.0.5 on 2021-03-22 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userconfirmation',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
