# Generated by Django 5.1.1 on 2024-11-08 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roupa', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roupa',
            name='materiais',
        ),
    ]
