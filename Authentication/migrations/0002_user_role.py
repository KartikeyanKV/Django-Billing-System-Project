# Generated by Django 5.1.3 on 2024-11-13 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.IntegerField(choices=[(0, 'Admin'), (1, 'Manager'), (2, 'Employee')], default=0),
        ),
    ]
