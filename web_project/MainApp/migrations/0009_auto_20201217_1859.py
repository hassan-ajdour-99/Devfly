# Generated by Django 3.1.4 on 2020-12-17 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0008_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='massages',
            new_name='message',
        ),
    ]
