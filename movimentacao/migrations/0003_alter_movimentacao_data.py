# Generated by Django 5.1.1 on 2024-11-08 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movimentacao', '0002_remove_movimentacao_codigo_roupa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movimentacao',
            name='data',
            field=models.DateField(),
        ),
    ]
