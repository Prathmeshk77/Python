# Generated by Django 2.2.5 on 2019-10-12 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='descriptin',
            new_name='description',
        ),
    ]