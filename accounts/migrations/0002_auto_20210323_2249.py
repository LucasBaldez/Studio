# Generated by Django 3.1.7 on 2021-03-24 01:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuarios',
            old_name='Usuario',
            new_name='usuario',
        ),
    ]