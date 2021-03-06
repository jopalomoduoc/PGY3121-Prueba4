# Generated by Django 3.2.4 on 2021-06-19 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de categoria')),
                ('nombreCategoria', models.CharField(max_length=50, verbose_name='Nombre de la categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('ISBN', models.CharField(max_length=13, primary_key=True, serialize=False, verbose_name='Codigo')),
                ('nombreLibro', models.CharField(max_length=255, verbose_name='Nombre del libro')),
                ('descripcion', models.CharField(blank=True, max_length=255, null=True, verbose_name='Descripcion')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.categoria')),
            ],
        ),
    ]
