# Generated by Django 4.1.2 on 2022-10-28 15:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_userdata_date_joined_alter_userdata_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined'),
        ),
    ]
