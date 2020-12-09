# Generated by Django 3.1.3 on 2020-12-08 11:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('restaurant', '0016_auto_20201204_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='waiter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Waiter',
        ),
    ]
