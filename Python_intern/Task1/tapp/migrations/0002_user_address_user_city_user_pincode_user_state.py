# Generated by Django 5.0.1 on 2024-01-09 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(default='Jaipur', max_length=200),
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(default='Jaipur', max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='pincode',
            field=models.CharField(default=303706, max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='state',
            field=models.CharField(default='Rajasthan', max_length=100),
        ),
    ]
