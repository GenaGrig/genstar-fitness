# Generated by Django 4.2.3 on 2023-08-06 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_membership'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='service',
            new_name='workout',
        ),
    ]
