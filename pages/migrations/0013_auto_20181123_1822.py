# Generated by Django 2.1 on 2018-11-23 18:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0012_remove_menu_item_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordercreated',
            name='amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ordercreated',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]