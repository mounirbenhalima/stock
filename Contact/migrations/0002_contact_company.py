# Generated by Django 4.0.4 on 2022-05-25 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='company',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Entreprise'),
        ),
    ]
