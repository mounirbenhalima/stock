# Generated by Django 3.1 on 2021-11-03 20:55

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Company', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Machine', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Marque')),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'Marque',
                'verbose_name_plural': 'Marques',
                'db_table': 'Brand',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Couleur')),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'Couleur',
                'verbose_name_plural': 'Couleurs',
                'db_table': 'Color',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='CombinedRange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, max_length=255, null=True)),
                ('capacity', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Capacité (L)')),
                ('link', models.CharField(blank=True, choices=[('AVEC_LIEN', 'Avec lien'), ('SANS_LIEN', 'Sans lien'), (None, '--------')], max_length=250, null=True, verbose_name='Lien de fermeture')),
                ('perfume', models.CharField(blank=True, choices=[('NOT_PERFUMED', 'Non Parfumé'), ('PERFUMED', 'Parfumé')], max_length=250, null=True)),
                ('type_name', models.CharField(blank=True, choices=[(None, '---------'), ('HAUTE_DENSITE', 'Haute Densité'), ('BASSE_DENSITE', 'Basse Densité'), ('LINEAIRE', 'Linéaire'), ('AUTRE', 'Autre')], max_length=250, null=True)),
                ('category', models.CharField(blank=True, choices=[('RAW_MATTER', 'Matière Première'), ('FINAL_PRODUCT', 'Produit Fini')], max_length=250, null=True)),
            ],
            options={
                'ordering': ['range_name', 'capacity', 'link'],
            },
        ),
        migrations.CreateModel(
            name='Flavor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Parfum')),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'Parfum',
                'verbose_name_plural': 'Parfums',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Handle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, max_length=255, null=True)),
                ('quantity', models.PositiveIntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Quantité')),
                ('threshold', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Seuil')),
                ('quantity_workshop', models.PositiveIntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name="Quantité dans l'atelier")),
                ('designation', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'ordering': ['brand', '-color'],
            },
        ),
        migrations.CreateModel(
            name='Labelling',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, max_length=255, null=True)),
                ('capacity', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='capacité')),
                ('link', models.CharField(blank=True, choices=[('AVEC_LIEN', 'Avec lien'), ('SANS_LIEN', 'Sans lien'), (None, '--------')], max_length=250, null=True, verbose_name='Lien de fermeture')),
                ('perfume', models.CharField(blank=True, choices=[('NOT_PERFUMED', 'Non Parfumé'), ('PERFUMED', 'Parfumé')], max_length=250, null=True)),
                ('quantity', models.PositiveIntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Quantité')),
                ('threshold', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Seuil')),
                ('quantity_workshop', models.PositiveIntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name="Quantité dans l'atelier")),
                ('designation', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'ordering': ['name', 'capacity'],
            },
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, max_length=255, null=True)),
                ('capacity', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='capacité')),
                ('link', models.CharField(blank=True, choices=[('AVEC_LIEN', 'Avec lien'), ('SANS_LIEN', 'Sans lien'), (None, '--------')], max_length=250, null=True, verbose_name='Lien de fermeture')),
                ('perfume', models.CharField(blank=True, choices=[('NOT_PERFUMED', 'Non Parfumé'), ('PERFUMED', 'Parfumé')], max_length=250, null=True)),
                ('quantity', models.PositiveIntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Quantité')),
                ('threshold', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Seuil')),
                ('quantity_workshop', models.PositiveIntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name="Quantité dans l'atelier")),
                ('designation', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'ordering': ['name', 'capacity'],
            },
        ),
        migrations.CreateModel(
            name='Range',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Gamme',
                'verbose_name_plural': 'Gammes',
                'db_table': 'Range',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='SparePart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Désignation ENG')),
                ('name_fr', models.CharField(blank=True, max_length=200, null=True, verbose_name='Désignation FR')),
                ('ref', models.CharField(blank=True, max_length=200, null=True, unique=True, verbose_name='Référence')),
                ('quantity', models.PositiveIntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Quantité')),
                ('threshold', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Seuil')),
                ('price', models.FloatField(blank=True, null=True, verbose_name='Prix')),
                ('category', models.CharField(blank=True, choices=[('ELECTRIQUE', 'Electrique'), ('ELECTRONIQUE', 'Electronique'), ('MECANIQUE', 'Mécanique'), ('PNEUMATIQUE', 'Pneumatique'), ('HYDROLIQUE', 'Hydrolique'), ('AUTRE', 'AUTRE')], max_length=200, null=True, verbose_name='Catégorie')),
            ],
        ),
        migrations.CreateModel(
            name='Trash',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, max_length=255, null=True)),
                ('ref', models.CharField(blank=True, max_length=255, null=True, verbose_name='Référence')),
                ('trash_type', models.CharField(blank=True, choices=[('HAUTE_DENSITE', 'Haute Densité'), ('BASSE_DENSITE', 'Basse Densité')], max_length=250, null=True, verbose_name='Type de déchet')),
                ('weight', models.FloatField(blank=True, null=True)),
                ('confirmation_weight', models.FloatField(blank=True, null=True)),
                ('date', models.DateTimeField(null=True)),
                ('state', models.CharField(blank=True, choices=[('PENDING', 'En attente de validation'), ('VALIDATED', 'Validé')], max_length=255, null=True, verbose_name='Etat')),
                ('comment', models.CharField(blank=True, max_length=255, null=True, verbose_name='Source')),
                ('machine', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Machine.machine')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('whereabouts', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Company.company')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Tape',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, max_length=255, null=True)),
                ('quantity', models.PositiveIntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Quantité')),
                ('threshold', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Seuil')),
                ('quantity_workshop', models.PositiveIntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name="Quantité dans l'atelier")),
                ('tape_type', models.CharField(blank=True, choices=[('BIG', 'Grand Modèle'), ('SMALL', 'Petit Modèle')], default=0, max_length=255, null=True, verbose_name='Type')),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tape_brand', to='Product.brand', verbose_name='Marque')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, max_length=255, null=True)),
                ('ref', models.CharField(blank=True, max_length=200, null=True)),
                ('product_designation', models.CharField(blank=True, max_length=200, null=True)),
                ('weight', models.DecimalField(blank=True, decimal_places=1, default=0, max_digits=5, null=True)),
                ('quantity', models.IntegerField(blank=True, default=0, null=True, verbose_name='Quantité')),
                ('quantity_workshop', models.IntegerField(blank=True, default=0, null=True, verbose_name="Quantité dans l'atelier")),
                ('external_quantity', models.IntegerField(blank=True, default=0, null=True, verbose_name='Stock Externe')),
                ('threshold', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Seuil')),
                ('price', models.FloatField(blank=True, null=True, verbose_name='Prix')),
                ('type_name', models.CharField(blank=True, choices=[(None, '---------'), ('HAUTE_DENSITE', 'Haute Densité'), ('BASSE_DENSITE', 'Basse Densité'), ('LINEAIRE', 'Linéaire'), ('AUTRE', 'Autre')], max_length=250, null=True)),
                ('perfume', models.CharField(blank=True, choices=[('NOT_PERFUMED', 'Non Parfumé'), ('PERFUMED', 'Parfumé')], max_length=250, null=True)),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Product.brand', verbose_name='Marque')),
                ('color', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Product.color', verbose_name='Couleur')),
                ('combined_range', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Product.combinedrange')),
                ('flavor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Product.flavor', verbose_name='Parfum')),
                ('name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Product.range')),
            ],
            options={
                'verbose_name': 'Produit',
                'verbose_name_plural': 'Produits',
                'db_table': 'Product',
                'ordering': ['name__name', 'brand__name'],
            },
        ),
    ]
