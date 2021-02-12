from django.db import models

#estados = [ (1, 'chiapas'),(2, 'veracruz')]
# Create your models here.
class cliente(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    calle = models.CharField(max_length=200)
    colonia = models.CharField(max_length=200)
   # estado = models.IntegerField(
    #    null=False, blank=False,
    #    choices=estados
    #)
    municipio = models.CharField(max_length=200)
    coordenadas = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200)
    paquete = models.CharField(max_length=200)
    tarjeta = models.CharField(max_length=200)
    banco = models.CharField(max_length=200)
    titular = models.CharField(max_length=200)
    numero = models.CharField(max_length=200)
    fecha = models.CharField(max_length=200)
    codigo = models.CharField(max_length=200)
    cp = models.CharField(max_length=200)
    modem = models.CharField(max_length=200)
    lbn = models.CharField(max_length=200)
    instalacion = models.CharField(max_length=200)
    mac = models.CharField(max_length=200)


class album(models.Model):
    # owner = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(verbose_name="Imagen",upload_to="albums")
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name="Fecha de edición")
    
    class Meta:
        verbose_name = "Album"
        verbose_name_plural = "trabajos"
        ordering = ["-created"]


    def __unicode__(self,):
        return self.title