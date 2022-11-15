# Generated by Django 3.2.3 on 2021-06-07 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medecin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('motdepasse', models.CharField(max_length=16)),
                ('genre', models.CharField(max_length=10)),
                ('numTel', models.CharField(max_length=100)),
                ('adresse', models.CharField(max_length=100)),
                ('dateNaissance', models.DateField()),
                ('specialite', models.CharField(max_length=50)),
            ],
        ),
    ]
