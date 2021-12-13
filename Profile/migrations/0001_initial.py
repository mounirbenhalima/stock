# Generated by Django 3.1 on 2021-11-03 20:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Company', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='JobPosition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True, unique=True, verbose_name='Intitulé du poste')),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Poste',
                'verbose_name_plural': 'Postes',
                'db_table': 'JobPosition',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, max_length=255, null=True)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('base_salary', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('salary', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('bonus', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('iep', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('irg', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('panier', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('ss', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('trans', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('net', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('cotisable', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('imposable', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('holiday', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('valid', models.BooleanField(blank=True, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Utilisateur')),
            ],
            options={
                'verbose_name': 'Salary',
                'verbose_name_plural': 'Salaries',
                'db_table': 'Salary',
                'ordering': ['valid', '-date'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, null=True)),
                ('group', models.IntegerField(blank=True, null=True)),
                ('hiring_date', models.DateField(blank=True, null=True)),
                ('bonus', models.DecimalField(blank=True, decimal_places=1, max_digits=5, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Image')),
                ('birth_day', models.DateField(blank=True, null=True, verbose_name='Date de Naissance')),
                ('mobile', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('rest_holiday', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('salary', models.DecimalField(blank=True, decimal_places=1, max_digits=10, null=True)),
                ('self_transported', models.BooleanField(blank=True, default=False, null=True)),
                ('active', models.BooleanField(blank=True, default=True, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Company.company')),
                ('job_position', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Profile.jobposition', verbose_name='Postes')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Utilisateur')),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
                'db_table': 'Profile',
                'ordering': ['group'],
            },
        ),
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, max_length=255, null=True)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('duration', models.DecimalField(blank=True, decimal_places=1, max_digits=5, null=True)),
                ('hours', models.DecimalField(blank=True, decimal_places=0, max_digits=5, null=True)),
                ('minutes', models.DecimalField(blank=True, decimal_places=0, max_digits=5, null=True)),
                ('quality', models.DecimalField(blank=True, decimal_places=1, default=0, max_digits=5, null=True)),
                ('quantity', models.DecimalField(blank=True, decimal_places=1, default=0, max_digits=5, null=True)),
                ('motivation', models.DecimalField(blank=True, decimal_places=1, default=0, max_digits=5, null=True)),
                ('attitude', models.DecimalField(blank=True, decimal_places=1, default=0, max_digits=5, null=True)),
                ('punctuality', models.DecimalField(blank=True, decimal_places=1, default=0, max_digits=5, null=True)),
                ('look', models.DecimalField(blank=True, decimal_places=1, default=0, max_digits=5, null=True)),
                ('penality', models.DecimalField(blank=True, decimal_places=1, default=0, max_digits=5, null=True)),
                ('prime', models.DecimalField(blank=True, decimal_places=1, default=0, max_digits=5, null=True)),
                ('absence', models.DecimalField(blank=True, decimal_places=1, max_digits=5, null=True)),
                ('holiday', models.BooleanField(blank=True, null=True)),
                ('is_absent', models.BooleanField(blank=True, null=True)),
                ('valid', models.BooleanField(blank=True, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Utilisateur')),
            ],
            options={
                'verbose_name': 'Pointage',
                'verbose_name_plural': 'Pointages',
                'db_table': 'Point',
                'ordering': ['user', 'start_date'],
            },
        ),
        migrations.CreateModel(
            name='HolidayRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, max_length=255, null=True)),
                ('request_date', models.DateTimeField(null=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('validation_date', models.DateTimeField(null=True)),
                ('duration', models.IntegerField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Adresse')),
                ('mobile', models.CharField(blank=True, max_length=20, null=True)),
                ('motive', models.CharField(blank=True, choices=[('ANNUAL', 'Congé Annuel'), ('MARRIAGE', 'Mariage'), ('BIRTH', 'Naissance'), ('HEALTH', 'Problème de Santé'), ('OTHER', 'Autre')], max_length=255, null=True)),
                ('state', models.CharField(blank=True, choices=[('PENDING', 'En Attente'), ('ACCEPTED', 'Validé'), ('REJECTED', 'Rejeté')], max_length=255, null=True)),
                ('substitute', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='substitute_holiday', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='holiday_requester', to=settings.AUTH_USER_MODEL, verbose_name='Utilisateur')),
                ('validator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='holiday_validator', to=settings.AUTH_USER_MODEL, verbose_name='Utilisateur')),
            ],
            options={
                'verbose_name': 'Congé',
                'verbose_name_plural': 'Congés',
                'db_table': 'Holiday',
                'ordering': ['-state', 'request_date'],
            },
        ),
    ]
