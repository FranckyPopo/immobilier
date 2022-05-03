# Generated by Django 4.0.4 on 2022-05-03 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_ad', '0010_postad_user_id_ad_alter_postad_estate_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postad',
            name='estate_type',
            field=models.CharField(choices=[('Renting', 'Location'), ('Purchasing', 'Vente')], max_length=25),
        ),
    ]