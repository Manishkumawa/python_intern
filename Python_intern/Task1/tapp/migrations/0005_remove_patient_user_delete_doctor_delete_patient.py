# Generated by Django 5.0.1 on 2024-01-09 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tapp', '0004_alter_user_address_alter_user_city_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='user',
        ),
        migrations.DeleteModel(
            name='Doctor',
        ),
        migrations.DeleteModel(
            name='Patient',
        ),
    ]
