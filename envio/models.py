from django.db import models

# Create your models here.

class Centro(models.Model):
    """ Modela a los Centros de la UZ """

    LOCALIDADES_CHOICES = ( 
    	('-', 'DESCONOCIDA'),
    	('Z', 'ZARAGOZA'),
        ('T', 'TERUEL'),
        ('H', 'HUESCA'),
        ('A', 'LA ALMUNIA')
    )

    cid = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=250)
    localidad = models.CharField(max_length=1, choices=LOCALIDADES_CHOICES, default='-')
    url = models.URLField(default='http://unizar.es')

    def __str__(self):
        return("{}".format(self.nombre))
