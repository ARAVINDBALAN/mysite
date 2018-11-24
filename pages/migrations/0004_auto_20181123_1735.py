# Generated by Django 2.1.3 on 2018-11-23 12:05

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_menu_ordered'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='owners',
            field=models.ManyToManyField(blank=True, related_name='ownersofmenu', to=settings.AUTH_USER_MODEL),
        ),
    ]
