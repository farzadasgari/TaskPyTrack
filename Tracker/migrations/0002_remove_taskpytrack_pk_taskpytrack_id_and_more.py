# Generated by Django 5.0.4 on 2024-04-09 03:10

import Tracker.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tracker', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskpytrack',
            name='Pk',
        ),
        migrations.AddField(
            model_name='taskpytrack',
            name='id',
            field=models.BigAutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='taskpytrack',
            name='File',
            field=models.FileField(blank=True, upload_to=Tracker.models.create_with_pk),
        ),
    ]
