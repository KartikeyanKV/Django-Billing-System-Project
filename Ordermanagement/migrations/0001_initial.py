# Generated by Django 5.1.3 on 2024-11-12 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_name', models.CharField(max_length=200, null=True)),
                ('order_date', models.DateField(null=True)),
            ],
        ),
    ]
