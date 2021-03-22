from django.db import models

# Create your models here.
class Produit(models.Model):
    name=models.CharField(max_length=200, unique=True)
    quantite=models.IntegerField(null=True)
    securite = models.IntegerField(null=True)
    alerte = models.IntegerField(null=True)

    def __str__(self):
        return self.name

class Image(models.Model):
    name=models.CharField(max_length=200, unique=True)



