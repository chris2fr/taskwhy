# Generated by Django 2.1.4 on 2018-12-07 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('why', '0002_auto_20181207_0456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='what',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]
