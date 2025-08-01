# Generated by Django 5.0.6 on 2025-07-09 21:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecursoMedico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre del recurso')),
                ('tipo', models.CharField(choices=[('MED', 'Medicamento'), ('INS', 'Insumo médico'), ('EQU', 'Equipo médico')], max_length=3, verbose_name='Tipo')),
                ('cantidad', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Cantidad en stock')),
                ('lote', models.CharField(max_length=20, verbose_name='Número de lote')),
                ('fecha_vencimiento', models.DateField(verbose_name='Fecha de vencimiento')),
                ('proveedor', models.CharField(max_length=100, verbose_name='Proveedor')),
                ('estado', models.CharField(choices=[('DISP', 'Disponible'), ('AGOT', 'Agotado'), ('VENC', 'Vencido')], default='DISP', max_length=4, verbose_name='Estado')),
                ('creado', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de registro')),
                ('actualizado', models.DateTimeField(auto_now=True, verbose_name='Última actualización')),
            ],
            options={
                'verbose_name': 'Recurso Médico',
                'verbose_name_plural': 'Recursos Médicos',
                'ordering': ['-creado'],
                'indexes': [models.Index(fields=['tipo', 'estado'], name='registro_re_tipo_115535_idx')],
            },
        ),
    ]
