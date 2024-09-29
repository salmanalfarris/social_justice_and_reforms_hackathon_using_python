# Generated by Django 5.0.6 on 2024-09-27 08:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LegalAidProvider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('provider_type', models.CharField(choices=[('lawyer', 'Lawyer'), ('organization', 'Organization')], max_length=20)),
                ('contact_info', models.TextField()),
                ('specialties', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('service_type', models.CharField(max_length=100)),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='legal_aid.legalaidprovider')),
            ],
        ),
    ]
