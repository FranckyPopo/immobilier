# Generated by Django 4.0.4 on 2022-05-03 11:26

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PostAd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estate_type', models.CharField(choices=[('Renting', 'Location'), ('Purchasing', 'Vente')], max_length=25)),
                ('title_ad', models.CharField(max_length=30)),
                ('description_ad', models.TextField(max_length=1000)),
                ('price_ad', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000000000)])),
                ('photo_ad', models.ImageField(upload_to='')),
                ('date_create_ad', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.CharField(max_length=150)),
                ('user_id_ad', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000000000)])),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post_ad.city')),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post_ad.house')),
            ],
        ),
    ]
