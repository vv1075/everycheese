# Generated by Django 3.1.1 on 2024-02-15 08:15

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cheeses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cheese',
            name='country_of_origin',
            field=django_countries.fields.CountryField(blank=True, max_length=2, verbose_name='Country of Origin'),
        ),
    ]
