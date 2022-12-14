# Generated by Django 4.0.4 on 2022-08-27 00:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addres', models.CharField(max_length=250)),
                ('number', models.CharField(max_length=15)),
                ('locality', models.CharField(max_length=250)),
                ('zipcode', models.CharField(max_length=15)),
                ('complement', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=250)),
                ('type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('document', models.CharField(max_length=50)),
                ('birthday', models.DateField()),
                ('phone', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=4, max_digits=99999)),
                ('commision', models.DecimalField(decimal_places=4, max_digits=100)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_agent', to='imobile.person')),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_buyer', to='imobile.person')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_seller', to='imobile.person')),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField()),
                ('value', models.DecimalField(decimal_places=4, max_digits=99999)),
                ('commision', models.DecimalField(decimal_places=4, max_digits=100)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='imobile.adress')),
                ('features', models.ManyToManyField(blank=True, to='imobile.feature')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='imobile.person')),
            ],
        ),
        migrations.CreateModel(
            name='Options',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=250)),
                ('feature', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='imobile.feature')),
            ],
        ),
    ]
