from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

# Automatically save/update Personas when we create/update User instances
from django.db.models.signals import post_save
from django.dispatch import receiver

import os
from django.utils.text import slugify

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

    cid = models.IntegerField(_('Codigo de Centro'), primary_key=True)
    nombre = models.CharField(max_length=250)
    localidad = models.CharField(max_length=1, choices=LOCALIDADES_CHOICES, default='-')
    url = models.URLField(_('Página web del centro'), default='http://unizar.es')

    def __str__(self):
        return(self.nombre)


class Estudio(models.Model):
	""" Modela los distintos estudios de la UZ """

	TIPOS_ESTUDIO_CHOICES = (
        (5, _('Grado')),
        (6, _('Máster')),
    )
	eid = models.IntegerField(_('Código de Estudio'), primary_key=True)
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

    pid = models.IntegerField(_('Código de Plan'), primary_key=True)
    curso = models.CharField(max_length=4, choices=CURSOS_CHOICES) 
    estudio = models.ForeignKey(Estudio, on_delete=models.CASCADE)
    centro = models.ForeignKey(Centro, on_delete=models.CASCADE)
    
    def __str__(self):
        return("{} - {}".format(self.pid, self.estudio))


class Persona(models.Model):
    """ Modela a las personas """
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    nip = models.IntegerField('NIP', null=True, blank=True, validators = [MaxValueValidator(999999), MinValueValidator(100000)])
    planes = models.ManyToManyField(Plan, through='Matricula')
    

    def __str__(self):
        return("({}) - {}".format(self.nip, self.user))


    # refer to "Populating users" @ https://django-auth-ldap.readthedocs.io/en/latest/users.html
    # also could be done using signal @receiver(django_auth_ldap.backend.populate_user) 
    # cheking @ shell
    #   from django.contrib.auth import authenticate
    #   u1 = authenticate(username="UNIZARUSERNAME",password="UNIZARPASSWORD")
    @receiver(post_save, sender=User)
    def create_user_persona(sender, instance, created, **kwargs):
        if created: #first time a user logs ins, after user is saved...
            try:
                nip = int(instance.ldap_user.attrs.get("uidNumber")[0])
                # ToDo link Persona with their Matriculas, in real time here, querying SIGM@, or prepopulate some way
                Persona.objects.create(user=instance, nip=nip)
            except (KeyError, IndexError):
                Persona.objects.create(user=instance)
                #print("Error al obtener el nip desde el ldap, se guardara sin NIP")
        else:
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
        verbose_name = _('Matrícula')
        verbose_name_plural = _('Matrículas')

    def __str__(self):
        return(_("{} está matriculado en el plan {}".format(self.persona, self.plan)))

    def get_nombre_estudio(self):
        return self.plan.estudio.nombre


class Departamento(models.Model):
    """ Modela los Departamentos de la UZ """

    did = models.IntegerField(_('Código del Departamento'), primary_key=True)
    nombre = models.CharField(max_length=5000)

    def __str__(self):
        return self.nombre

def user_upload_anexos_directory_path(instance, filename):
    """ Returns a path where the file will be saved """
    # file will be uploaded to MEDIA_ROOT/trabajos-depositados/user_<id>/<filename>
    return 'trabajos-depositados/user_{0}/anexos-{1}'.format(instance.matricula.persona.user.id, slugify(filename))

def user_upload_memoria_directory_path(instance, filename):
    """ Returns a path where the file will be saved """
    # file will be uploaded to MEDIA_ROOT/trabajos-depositados/user_<id>/<filename>
    return 'trabajos-depositados/user_{0}/memoria-{1}'.format(instance.matricula.persona.user.id, slugify(filename))


class Entrega(models.Model):
    """ Modela las Entregas de trabajos que realiza una Persona """

    LICENSE_CHOICES = ( 
        (0, _('No autoriza consulta pública')),
        (1, _('Autoriza consulta pública')),
    )

    tid = models.AutoField(_('Código de entrega'), primary_key=True)
    titulo = models.CharField(max_length=500)
    resumen = models.CharField(max_length=5000)
    resumen_en = models.CharField(max_length=5000)
    notas = models.CharField(max_length=5000, null=True, blank=True)
    #Todo keywords as manytomanyfield?
    #ToDo director(es)
    #ToDo director(es) delegado(s)
    departamentos = models.ManyToManyField(Departamento)
    license = models.IntegerField(choices=LICENSE_CHOICES, default=0)
    matricula = models.ForeignKey(Matricula, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now=True)
    memoria = models.FileField(upload_to=user_upload_memoria_directory_path)
    anexos = models.FileField(null=True, blank=True, upload_to=user_upload_anexos_directory_path)
    entrega_material_adicional = models.BooleanField(default=False)
    
    def __str__(self):
        return(_("{} - Entrega {} del alumno {}").format(self.fecha, self.tid, self.matricula.persona))

    class Meta:
        verbose_name = _('Entrega')
        verbose_name_plural = _('Entregas')

@receiver(models.signals.post_delete, sender=Entrega)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding 'Entrega' object is deleted.
    Refactor? Perhaps it would be better to use django-cleanup https://github.com/un1t/django-cleanup
    """
    if instance.memoria:
        if os.path.isfile(instance.memoria.path):
            os.remove(instance.memoria.path)
    if instance.anexos:
        if os.path.isfile(instance.anexos.path):
            os.remove(instance.anexos.path)
            
@receiver(models.signals.pre_save, sender=Entrega)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem when corresponding 'Entrega' object is updated with new file.
    This function assumes that EVERY entrega has a mandatory 'memoria' field!!
    Refactor? Perhaps it would be better to use django-cleanup https://github.com/un1t/django-cleanup
    """
    if not instance.pk:
        return False

    try:
        old_memoria = Entrega.objects.get(pk=instance.pk).memoria
    except Entrega.DoesNotExist:
        return False
    new_memoria = instance.memoria
    if new_memoria and not old_memoria == new_memoria:
        if os.path.isfile(old_memoria.path):
            os.remove(old_memoria.path)
    
    old_anexos = None
    try:
        old_anexos = Entrega.objects.get(pk=instance.pk).anexos
    except Entrega.DoesNotExist:
        return False
    # if there were NO old_anexos, no need to do nothing...
    if not old_anexos:
        return True
    # if there were old_anexos, remove them... 
    new_anexos = instance.anexos
    if new_anexos and not old_anexos == new_anexos:
        if os.path.isfile(old_anexos.path):
            os.remove(old_anexos.path)




