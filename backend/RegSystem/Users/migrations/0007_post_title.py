# Generated by Django 2.2.5 on 2020-11-11 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0006_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
    ]
