# Generated by Django 4.1.7 on 2023-04-05 11:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('brand_category', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='brands',
            name='brand_intro',
            field=models.CharField(default=django.utils.timezone.now, max_length=400),
            preserve_default=False,
        ),
    ]
