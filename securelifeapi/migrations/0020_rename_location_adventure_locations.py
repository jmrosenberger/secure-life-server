# Generated by Django 3.2.10 on 2021-12-23 05:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('securelifeapi', '0019_auto_20211222_2239'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adventure',
            old_name='location',
            new_name='locations',
        ),
    ]