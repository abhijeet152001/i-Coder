# Generated by Django 3.1.4 on 2020-12-17 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogging', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.CharField(default='', max_length=120),
            preserve_default=False,
        ),
    ]
