# Generated by Django 3.2.10 on 2021-12-23 05:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('securelifeapi', '0020_rename_location_adventure_locations'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adventure',
            old_name='locations',
            new_name='location',
        ),
    ]