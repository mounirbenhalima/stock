# Generated by Django 3.1 on 2021-11-03 21:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0003_coil_coiltype_finishedproduct_finishedproducttype_rawmatter'),
        ('Production', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gaprawmatter',
            name='rawmatter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Product.rawmatter'),
        ),
        migrations.AddField(
            model_name='inkconsumption',
            name='ink',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ink_consumed', to='Product.rawmatter'),
        ),
        migrations.AddField(
            model_name='production',
            name='coil',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Bobine', to='Product.coil'),
        ),
        migrations.AddField(
            model_name='production',
            name='coil_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='BobineCible', to='Product.coiltype'),
        ),
        migrations.AddField(
            model_name='production',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ProduitCible', to='Product.finishedproducttype'),
        ),
    ]
