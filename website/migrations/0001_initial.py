# Generated by Django 4.1.7 on 2023-04-08 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('niveles_cursados', models.IntegerField()),
                ('puntuacion_media', models.IntegerField()),
            ],
        ),
    ]
