from django.db import models
#se importan el modelo Usuario que viene por defecto en Django
from django.contrib.auth.models import User
#se importa la zona horaria 
from django.utils import timezone 

#modelo clases temporal para uso de pruebas usuario AWRC
class Clases(models.Model):
	codigo = models.CharField(max_length=10, primary_key=True)
	tema = models.CharField(max_length=100)
	nombre = models.CharField(max_length=100)

	def __str__(self):
		return f'Tema: {self.tema} código:{self.codigo}'

#Creación del modelo para los perfiles de los usuarios
class Profile(models.Model):
	'''
	Atributos de Profile
	on_delete es por si ADMIN elimina un usuario también se elimina con el perfil
	'''
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	#equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, null=False, blank=False, default=None)
	#image = models.ImageField(default="profile.png")

	def __str__(self):
		return f'Perfil de {self.user.username}'

class Equipo(models.Model):
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)
	numEquipo = models.IntegerField(default=None,primary_key=True)


#Creación del modelo para los post de los alumnos en los pasos de MG
class Post(models.Model):
	'''
	Atributos de Post
	'''
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post')
	timestamp = models.DateTimeField(default = timezone.now) 
	content = models.TextField()
	voto = models.IntegerField(default=0)
	comentario = models.TextField(default='')
	#codigo_materia = models.ForeignKey(Clases, on_delete=models.CASCADE)

	class Meta:
		ordering = ['-timestamp']
	#str necesario para visualizar el contenido del post en local/admin/post
	def __str__(self):
		return f'{self.user.username}: {self.content}'

#Creación del modelo para los post de los alumnos en los pasos de MG
class PostSecundaria(models.Model):
	'''
	Atributos de Post
	'''
	userSecu = models.ForeignKey(User, on_delete=models.CASCADE, related_name='postSecu')
	timestampSecu = models.DateTimeField(default = timezone.now) 
	contentSecu = models.TextField()
	votoSecu = models.IntegerField(default=0)
	comentarioSecu = models.TextField(default='')
	#codigo_materia = models.ForeignKey(Clases, on_delete=models.CASCADE)

	class Meta:
		ordering = ['-timestampSecu']
	#str necesario para visualizar el contenido del post en local/admin/post
	def __str__(self):
		return f'{self.user.username}: {self.content}'

class Anadir(models.Model):
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)
	codigo_materia = models.ForeignKey(Clases, on_delete=models.CASCADE)

class Votar(models.Model):
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)
	codigo_materia = models.ForeignKey(Clases, on_delete=models.CASCADE)



