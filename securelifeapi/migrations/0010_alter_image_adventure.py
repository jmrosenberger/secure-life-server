# Generated by Django 3.2.10 on 2021-12-17 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('securelifeapi', '0009_auto_20211216_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='adventure',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='securelifeapi.adventure'),
        ),
    ]
