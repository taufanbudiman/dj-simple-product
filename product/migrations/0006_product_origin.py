# Generated by Django 4.2.13 on 2024-07-05 06:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_rename_masterspecies_origin_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='origin',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.origin'),
        ),
    ]
