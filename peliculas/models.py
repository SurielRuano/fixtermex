from django.db import models

# Create your models here.



class Cine(models.Model):

	lugar = models.CharField(max_length=100)
	geolocalizacion = models.CharField(max_length= 80,blank=True, null=True)
	def __str__(self):

		return self.lugar


class Pelicula(models.Model):

	CLASIFICACIONES = (('A','Infantil'),('B','Adolecentes'),('C','Adultos'))
	titulo = models.CharField(max_length=100)
	sinopsis = models.TextField()
	clasificacion =models.CharField(max_length=3,choices=CLASIFICACIONES)
	imagen = models.ImageField(upload_to='img_pelicula')
	

	def __str__(self):

		return self.titulo

class Horario(models.Model):

	horario = models.CharField(max_length=6)
	cine = models.ForeignKey(Cine)
	pelicula = models.ForeignKey(Pelicula)
	def __str__(self):

		return self.horario





## ManyToManyField  muchos a muchos
## ForeignKey
## OneToOneField
