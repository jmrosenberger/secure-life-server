# Generated by Django 3.2.10 on 2021-12-14 21:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('securelifeapi', '0005_remove_human_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adventure',
            name='human',
        ),
        migrations.AddField(
            model_name='human',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='humans', to='auth.user'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adventure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='securelifeapi.adventure')),
                ('human', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='securelifeapi.human')),
            ],
        ),
        migrations.AddField(
            model_name='adventure',
            name='participants',
            field=models.ManyToManyField(through='securelifeapi.Participant', to='securelifeapi.Human'),
        ),
    ]