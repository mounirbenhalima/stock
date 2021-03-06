# Generated by Django 4.0.4 on 2022-05-24 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=255)),
                ('last_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Nom de Famille')),
                ('first_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Prénom')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=10, null=True, verbose_name='Numero de Téléphone')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Adresse')),
                ('region', models.CharField(blank=True, max_length=255, null=True, verbose_name='Wilaya')),
            ],
            options={
                'verbose_name': 'Supplier',
                'verbose_name_plural': 'Suppliers',
                'db_table': 'Supplier',
                'ordering': ['first_name'],
            },
        ),
    ]
