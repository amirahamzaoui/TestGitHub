from django.db import models

# Create your models here.

class Jobseeker (models.Model):
    SEXE_GENDER = (
    ('F', 'Feminin'),
    ('M', 'Masculin'),    
)
    ETAT_CIVIL_CHOICES = (
    ('Celibataire', 'Celibataire'),
    ('Marie', 'Marie'),      
)
    prenom = models.CharField(max_length=200)
    nom = models.CharField(max_length=200)
    sexe = models.CharField(choices=SEXE_GENDER, max_length=1)
    date_naissance = models.DateField(auto_now=True)
    etat_civil = models.CharField(choices=ETAT_CIVIL_CHOICES, max_length=1, default = "False")
    nationalite = models.CharField(max_length=200)
    adresse = models.CharField(max_length=200)
    code_postal = models.IntegerField()
    telephone = models.CharField(max_length=8)
    msg_instantanne = models.CharField(max_length = 200)
    permis_conduire = models.BooleanField(default = "False")
    titulaire_voitre = models.BooleanField(default = "False")
    avoir_handicap =  models.BooleanField(default = "False")