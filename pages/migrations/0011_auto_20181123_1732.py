# Generated by Django 2.1 on 2018-11-23 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0010_auto_20181123_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordercreated',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.student'),
        ),
    ]