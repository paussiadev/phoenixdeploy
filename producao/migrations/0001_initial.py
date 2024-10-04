# Generated by Django 5.1.1 on 2024-10-03 13:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('roupa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('data', models.DateTimeField()),
                ('valorTotal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('roupa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roupa.roupa')),
            ],
        ),
    ]