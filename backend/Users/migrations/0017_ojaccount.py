# Generated by Django 2.2.3 on 2020-12-11 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0016_auto_20201130_0217'),
    ]

    operations = [
        migrations.CreateModel(
            name='OJaccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=10)),
            ],
        ),
    ]
