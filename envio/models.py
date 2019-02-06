from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

# Automatically save/update Personas when we create/update User instances
from django.db.models.signals import post_save
from django.dispatch import receiver

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
	centros = models.ManyToManyField(Centro, through='Plan')

	def __str__(self):
		return("(%s) %s" %( self.eid, self.nombre ))


class Plan(models.Model):
    """ Modela las relaciones centro-estudio-plan-curso """

    CURSOS_CHOICES = ( 
        ('2017', '2017/2018'),
    	('2018', '2018/2019'),
    )

    pid = models.IntegerField('Código de Plan', primary_key=True)
    curso = models.CharField(max_length=4, choices=CURSOS_CHOICES) 
    estudio = models.ForeignKey(Estudio, on_delete=models.CASCADE)
    centro = models.ForeignKey(Centro, on_delete=models.CASCADE)
    
    def __str__(self):
        return("{} - {}".format(self.pid, self.estudio))


class Persona(models.Model):
    """ Modela a las personas """
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    nip = models.IntegerField('NIP UNIZAR', null=True, blank=True, validators = [MaxValueValidator(999999), MinValueValidator(100000)])
    planes = models.ManyToManyField(Plan, through='Matricula')
    

    def __str__(self):
        return("({}) - {}".format(self.nip, self.user))

    # ToDo Populate user info from ldap and other sources to get nip, matriculas and so on!!!
    # refer to "Populating users" @ https://django-auth-ldap.readthedocs.io/en/latest/users.html
    @receiver(post_save, sender=User)
    def create_user_persona(sender, instance, created, **kwargs):
        if created:
            Persona.objects.create(user=instance)

    # ToDo Populate user info from ldap and other sources to get nip, matriculas and so on!!!
    # refer to "Populating users" @ https://django-auth-ldap.readthedocs.io/en/latest/users.html
    @receiver(post_save, sender=User)
    def save_user_persona(sender, instance, **kwargs):
        instance.persona.save()

    def get_entregas(self):
        """ 
        Obtiene las entregas de una persona
        """
        return Entrega.objects.filter(matricula__persona=self) 


class Matricula(models.Model):
    """ Modela las matrículas de la persona """

    CURSOS_CHOICES = ( 
        ('2017', '2017/2018'),
        ('2018', '2018/2019'),
    )

    curso = models.CharField(max_length=4, choices=CURSOS_CHOICES)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)

    class Meta: # para que actuen como una constraint, como si fuera una PK formada por los 3 campos
        unique_together = (("curso", "persona", "plan"),)

    def __str__(self):
        return("{} está matriculado en el plan {}".format(self.persona, self.plan))

    def get_nombre_estudio(self):
        return self.plan.estudio.nombre

class Entrega(models.Model):
    """ Modela las Entregas de trabajos que realiza una Persona """

    tid = models.AutoField('Código de entrega', primary_key=True)
    titulo = models.CharField(max_length=500)
    resumen = models.CharField(max_length=5000)
    matricula = models.ForeignKey(Matricula, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now=True)

    def __str__(self):
        return("{} - Entrega {} del alumno {}".format(self.fecha, self.tid, self.matricula.persona))






