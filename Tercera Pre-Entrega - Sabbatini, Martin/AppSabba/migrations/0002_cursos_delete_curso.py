# Generated by Django 4.1.5 on 2023-02-09 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppSabba', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('comision', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Curso',
        ),
    ]
