# Generated by Django 4.0 on 2022-02-13 16:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0013_coil_micronnage_print_alter_coil_capacity_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='weight',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Poids'),
        ),
    ]