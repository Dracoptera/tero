# Generated by Django 3.0.3 on 2020-03-31 04:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, null=True)),
                ('tel', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('nacimiento', models.DateField(null=True)),
                ('altura', models.FloatField(null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, null=True)),
                ('dosis', models.FloatField(null=True)),
                ('tipo_dosis', models.CharField(choices=[('g', 'g'), ('mg', 'mg'), ('ml', 'ml'), ('Ul', 'Ul'), ('mcg', 'mcg'), ('mcg/ml', 'mcg/ml'), ('mEq', 'mEq'), ('%', '%'), ('mg/g', 'mg/g'), ('mg/cm2', 'mg/cm2'), ('mg/ml', 'mg/ml'), ('mcg/hora', 'mcg/hora')], max_length=200, null=True)),
                ('cantidad', models.IntegerField(null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, null=True)),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cuentas.Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Alarma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=200, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, null=True)),
                ('medicamento', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cuentas.Medicamento')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cuentas.Usuario')),
            ],
        ),
    ]
