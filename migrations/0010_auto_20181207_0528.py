# Generated by Django 2.1.4 on 2018-12-07 05:28

from django.conf import settings
from django.db import migrations, models
from datetime import datetime
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('why', '0009_auto_20181207_0520'),
    ]

    operations = [
        migrations.AddField(
            model_name='what',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=datetime(2018, 12, 7, 6, 33, 14, 849524)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='what',
            name='modified_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='who',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=datetime(2018, 12, 7, 6, 33, 14, 849524)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='who',
            name='modified_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='what',
            name='django_user_owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
