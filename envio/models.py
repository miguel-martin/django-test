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

    cid = models.IntegerField('Codigo de Centro', primary_key=True)
    nombre = models.CharField(max_length=250)
    localidad = models.CharField(max_length=1, choices=LOCALIDADES_CHOICES, default='-')
    url = models.URLField('Página web del centro', default='http://unizar.es')

    def __str__(self):
        return(self.nombre)


class Estudio(models.Model):
	""" Modela los distintos estudios de la UZ """
	TIPOS_ESTUDIO_CHOICES = (
        (5, 'Grado'),
        (6, 'Máster'),
    )
	eid = models.IntegerField('Código de Estudio', primary_key=True)
	nombre = models.CharField(max_length=250)
	tipo = models.IntegerField(choices=TIPOS_ESTUDIO_CHOICES)
	centros = models.ManyToManyField(Centro, through='Plan', default=5)

	def __str__(self):
		return("(%s) %s" %( self.eid, self.nombre ))


class Plan(models.Model):
    """ Modela las relaciones centro-estudio-plan-curso """

    CURSOS_CHOICES = ( 
    	('2018', '2018/2019'),
    )

    pid = models.IntegerField('Código de Plan')
    curso = models.CharField(max_length=4, choices=CURSOS_CHOICES) 
    estudio = models.ForeignKey(Estudio, on_delete=models.CASCADE)
    centro = models.ForeignKey(Centro, on_delete=models.CASCADE)
    
    def __str__(self):
        return("{} - {}".format(self.pid, self.estudio))


