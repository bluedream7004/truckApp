# Generated by Django 2.2.8 on 2021-07-24 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0013_auto_20210724_0549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='user_first_name',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='order',
            name='user_last_name',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]
