# Generated by Django 4.0.4 on 2022-05-01 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_ad', '0003_alter_postad_date_create_ad_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postad',
            name='date_create_ad',
            field=models.DateTimeField(auto_now=True, verbose_name='Date création'),
        ),
    ]