# Generated by Django 2.1.4 on 2018-12-07 05:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taskphrase', '0003_auto_20181207_0501'),
    ]

    operations = [
        migrations.AddField(
            model_name='what',
            name='django_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
