from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, PostForm, CodeForm
from django.contrib.auth import authenticate, login
from django.template import RequestContext
from django.contrib.auth.models import User
from .models import *
from django.urls import reverse
#se importa para aumentar el contador de votos en feed
from django.db.models import F

# Create your views here.

def index(request):
	return render(request, "AMCE/index.html")

def feed(request):
	#code = Anadir.objects.filter(codigo_materia_id=codigo,user_id_id=request.user.pk)
	posts = Post.objects.all();
	context = {'post':posts}
	#se consigue el valor de la celda voto del usuario 
	a = request.POST
	if request.method == 'POST':
		#se captura el nombre de usuario por el cual se está votando
		voto = request.POST.get("preguntaInicial")
		comentario = request.POST.get("comentario")
		print(comentario)
		#Se agrega voto y se agrega comentario a las respectivas celdas de la Bade de Datos
		voto_sumar = Post.objects.filter(user_id=voto).update(voto=F('voto')+1)
		comentario_agregar = Post.objects.filter(user_id=request.user.pk).update(comentario=comentario)
		return redirect('AMCE:retroalimentacionPI')
	return render(request, 'AMCE/feed.html', context)

def retroPreguntaInicial(request):
	posts = Post.objects.all();
	context = {'post':posts}
	return render(request, 'AMCE/retroPreguntaInicial.html', context)	

def feed1_2(request):
	posts = Post.objects.all();
	context = {'post':posts}
	return render(request, 'AMCE/Feed1/feed1_2.html', context)

@login_required
def MG1(request):
	#clases = Clases.objects.all()
	equipo = Equipo.objects.filter(numEquipo=1);
	print(equipo)
	if equipo == 2:
		print(1)
	else:
		print(2)
	anadir = Anadir()
	#Muestro las clases asignadas al ID del usuario actual
	code = Anadir.objects.filter(user_id_id=request.user.pk)
	a = request.POST
	current_user = get_object_or_404(User, pk=request.user.pk)
	args = {'form': a, 'code':code}
	if request.method == 'POST':
		print(a)
		codigo_ingresado = request.POST.get("new")
		anadir.codigo_materia = Clases.objects.get(codigo = request.POST.get("new"))
		codigo_clase = Anadir(user_id=current_user,codigo_materia=anadir.codigo_materia)
		#anadir.save()
		codigo_clase.save()


	return render(request,"AMCE/SelEquipo.html",args)

def registro(request):
	data = {
		'form': CustomUserCreationForm()
	}
	if request.method == "POST":
		formulario = CustomUserCreationForm(data=request.POST)
		if formulario.is_valid():
			usuario = formulario.save()
			usuario.save()
			user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
			equipo = Equipo.objects.all();

			login(request,user)
			messages.success(request, "Registro exitoso, inicia sesión")
			return redirect(to="AMCE:MG1")
		data["form"] = formulario
	return render(request,'registration/registro.html',data)

def agregarClase(request):
	form = CodeForm(request.POST)
	if form.is_valid():
		text = form.cleaned_data['code']
	context = {'form' : form}
	return render(request, 'AMCE/MG1.html', context)

#con pk adquirimos al usuario loggeado
def post1_1(request):
	'''
	Función para mostrar las actividades individuales de cada clase en la que 
	esté inscrito el alumno
	'''
	#cambiar a get
	#code = Anadir.objects.get(codigo_materia_id=codigo,user_id_id=request.user.pk)
	current_user = get_object_or_404(User, pk=request.user.pk)
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			#Agarramos los datos del usuario que ingresó datos en el forms
			post = form.save(commit=False)
			post.user = current_user
			post.save()
			messages.success(request, 'Post enviado')
			return redirect('AMCE:feed')
	else:
		form = PostForm()
	return render(request, 'AMCE/Paso1/post1-1.html', {'form': form})

def post1_2(request):
	#code = Anadir.objects.filter(codigo_materia_id=codigo)
	current_user = get_object_or_404(User, pk=request.user.pk)
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			#Agarramos los datos del usuario que ingresó datos en el forms
			post = form.save(commit=False)
			post.user = current_user
			post.save()
			messages.success(request, 'Post enviado')
			return redirect("/feed1-2")
	else:
		form = PostForm()
	return render(request, 'AMCE/Paso1/post1-2.html', {'form': form})

def post1_3(request):
	current_user = get_object_or_404(User, pk=request.user.pk)
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			#Agarramos los datos del usuario que ingresó datos en el forms
			post = form.save(commit=False)
			post.user = current_user
			post.save()
			messages.success(request, 'Post enviado')
			return redirect("AMCE:index")
	else:
		form = PostForm()
	return render(request, 'AMCE/Paso1/post1-3.html', {'form': form})

def post1_4(request):
	current_user = get_object_or_404(User, pk=request.user.pk)
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			#Agarramos los datos del usuario que ingresó datos en el forms
			post = form.save(commit=False)
			post.user = current_user
			post.save()
			messages.success(request, 'Post enviado')
			return redirect("AMCE:feed")
	else:
		form = PostForm()
	return render(request, 'AMCE/Paso1/post1-4.html', {'form': form})

#Función que crea un perfil cada que se crea un usuario

def profile(request,username=None):
	current_user = request.user
	#Preguntamos si el usuario loggeado quiere ver su perfil o un perfil de algún amigo
	if username and username != current_user.username:
		user = User.objects.get(username=username)
		posts = user.posts.all()
	else:
		post = current_user.posts.all()
		user = current_user
	return render(request, 'registration/profile.html', {'user': user, 'posts':posts})




