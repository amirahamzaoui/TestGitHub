# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jobseeker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('prenom', models.CharField(max_length=200)),
                ('nom', models.CharField(max_length=200)),
                ('sexe', models.CharField(max_length=1, choices=[(b'F', b'Feminin'), (b'M', b'Masculin')])),
                ('date_naissance', models.DateField(auto_now=True)),
                ('etat_civil', models.CharField(max_length=1, choices=[(b'Celibataire', b'Celibataire'), (b'Marie', b'Marie')])),
                ('nationalite', models.CharField(max_length=200)),
                ('adresse', models.CharField(max_length=200)),
            ],
        ),
    ]
