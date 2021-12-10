# Generated by Django 3.2.10 on 2021-12-09 20:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Human',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='humans', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.ImageField(upload_to='')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='states', to='securelifeapi.country')),
            ],
        ),
        migrations.CreateModel(
            name='Park',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parks', to='securelifeapi.state')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='locations', to='securelifeapi.city')),
                ('park', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='locations', to='securelifeapi.park')),
            ],
        ),
        migrations.CreateModel(
            name='JournalEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('human', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='journal_entries', to='securelifeapi.human')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='journal_entries', to='securelifeapi.image')),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='securelifeapi.tag'),
        ),
        migrations.CreateModel(
            name='HumanProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('length', models.IntegerField()),
                ('date', models.DateField()),
                ('human', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='human_progress', to='securelifeapi.human')),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cities', to='securelifeapi.state'),
        ),
        migrations.CreateModel(
            name='Adventure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('description', models.CharField(max_length=500)),
                ('human', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='adventures', to='securelifeapi.human')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='adventures', to='securelifeapi.image')),
            ],
        ),
    ]