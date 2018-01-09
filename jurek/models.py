from django.db import models

# Create your models here.
class Name(models.Model):
    name1 = models.CharField(max_length=30)
    name2 = models.CharField(max_length=30)

    def __str__(self):
        return ("Imie: "+self.name1+" Nazwisko : "+self.name2)

