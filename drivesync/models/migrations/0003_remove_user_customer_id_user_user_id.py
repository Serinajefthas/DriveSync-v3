# Generated by Django 4.2.7 on 2023-11-29 19:26

from django.db import migrations
from django.db import models as django_models
import models.user


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0002_alter_user_customer_id_alter_user_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='customer_id',
        ),
        migrations.AddField(
            model_name='user',
            name='user_id',
            field=django_models.CharField(default=models.user.generate_user_id, max_length=10),
        ),
    ]
