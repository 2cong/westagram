# Generated by Django 3.0.5 on 2020-04-10 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='reply',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
    ]