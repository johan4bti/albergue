# Generated by Django 5.2.2 on 2025-07-10 00:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0003_alter_recursomedico_actualizado_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recursomedico',
            name='lote',
        ),
    ]
