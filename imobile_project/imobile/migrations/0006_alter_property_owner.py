# Generated by Django 4.0.4 on 2022-08-30 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('imobile', '0005_remove_property_address_adress_property'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_owner', to='imobile.person'),
        ),
    ]
