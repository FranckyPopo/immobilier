# Generated by Django 4.0.4 on 2022-05-03 12:50

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post_ad', '0004_remove_postad_user_id_ad'),
    ]

    operations = [
        migrations.AddField(
            model_name='postad',
            name='number_of_piece',
            field=models.IntegerField(default=2, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000000000)]),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='SearchProperty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estate_type', models.CharField(choices=[('Renting', 'Location'), ('Purchasing', 'Vente')], max_length=25)),
                ('number_of_piece', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000000000)])),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post_ad.city')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post_ad.district')),
                ('property_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post_ad.house')),
            ],
        ),
    ]