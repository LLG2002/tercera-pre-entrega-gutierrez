# Generated by Django 4.2 on 2023-04-13 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=15)),
                ('contraseña', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=25)),
                ('edad', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Cliente',
        ),
    ]
