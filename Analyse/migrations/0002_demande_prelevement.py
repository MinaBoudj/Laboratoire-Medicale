# Generated by Django 3.2.3 on 2021-06-28 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Analyse', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prelevement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_demande', models.PositiveIntegerField()),
                ('nature_prelevement', models.CharField(max_length=200)),
                ('type_tube', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Demande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomPatient', models.CharField(max_length=200)),
                ('prenomPatient', models.CharField(max_length=200)),
                ('idPatient', models.PositiveIntegerField()),
                ('age', models.PositiveIntegerField()),
                ('service', models.CharField(max_length=200)),
                ('Nommedecin_demandeur', models.CharField(max_length=200)),
                ('Prenommedecin_demandeur', models.CharField(max_length=200)),
                ('date_ajout_demande', models.DateTimeField(auto_now_add=True)),
                ('nb_prelevement', models.PositiveIntegerField()),
                ('Biochimie', models.ManyToManyField(to='Analyse.AnalyseBiochimie')),
                ('Hémobiologie', models.ManyToManyField(to='Analyse.AnalyseHémobiologie')),
                ('Microbiologie', models.ManyToManyField(to='Analyse.AnalyseMicrobiologie')),
                ('Parasitologie', models.ManyToManyField(to='Analyse.AnalyseParasitologie')),
            ],
        ),
    ]
