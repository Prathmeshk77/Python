# Generated by Django 2.2.5 on 2019-10-12 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20191012_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]