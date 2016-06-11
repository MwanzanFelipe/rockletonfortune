# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-07 21:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BckGrnd_Clcs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_week_updated', models.IntegerField()),
                ('date_updated', models.DateField(verbose_name='Date of ReUp')),
            ],
        ),
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=7)),
                ('ed_perc', models.DecimalField(decimal_places=2, max_digits=5)),
                ('time_period', models.CharField(choices=[('WE', 'Weekly'), ('MO', 'Monthly')], default='WE', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Primary_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Category Name')),
            ],
        ),
        migrations.CreateModel(
            name='Primary_Category_Bucket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, verbose_name='Category Name')),
            ],
        ),
        migrations.CreateModel(
            name='Rockleton',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Secondary_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Category Name')),
                ('primary_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zillions.Primary_Category')),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Source Name')),
            ],
        ),
        migrations.CreateModel(
            name='Source_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, verbose_name='Category Name')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_date', models.DateField(verbose_name='Transaction Date')),
                ('description', models.CharField(max_length=60, verbose_name='Description')),
                ('original_description', models.CharField(blank=True, max_length=170, null=True, verbose_name='Original Description')),
                ('amount', models.DecimalField(decimal_places=4, max_digits=9)),
                ('transaction_type', models.IntegerField(choices=[(-1, 'debit'), (1, 'credit')])),
                ('ed_perc', models.DecimalField(decimal_places=2, max_digits=5)),
                ('notes', models.TextField(blank=True, verbose_name='Notes')),
                ('alias', models.CharField(blank=True, max_length=60, verbose_name='Alias')),
                ('mint_import', models.BooleanField(default=True)),
                ('internal_transfer', models.BooleanField(default=False)),
                ('flagged', models.BooleanField(default=False)),
                ('secondary_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zillions.Secondary_Category')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zillions.Source')),
            ],
            options={
                'ordering': ('-transaction_date',),
            },
        ),
        migrations.CreateModel(
            name='Transaction_Import',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_date', models.DateField(verbose_name='Transaction Date')),
                ('description', models.CharField(max_length=60, verbose_name='Description')),
                ('original_description', models.CharField(blank=True, max_length=170, null=True, verbose_name='Original Description')),
                ('amount', models.DecimalField(decimal_places=4, max_digits=9)),
                ('transaction_type', models.IntegerField(choices=[(-1, 'debit'), (1, 'credit')])),
                ('secondary_category', models.CharField(max_length=60, verbose_name='Secondary Category')),
                ('source', models.CharField(max_length=60, verbose_name='Source')),
            ],
            options={
                'ordering': ('-transaction_date',),
            },
        ),
        migrations.AddField(
            model_name='source',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zillions.Source_Category'),
        ),
        migrations.AddField(
            model_name='primary_category',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zillions.Primary_Category_Bucket'),
        ),
        migrations.AddField(
            model_name='budget',
            name='secondary_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zillions.Secondary_Category'),
        ),
        migrations.AddField(
            model_name='budget',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zillions.Rockleton'),
        ),
        migrations.AlterUniqueTogether(
            name='budget',
            unique_together=set([('user', 'secondary_category')]),
        ),
    ]