from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def home(request):
   title = 'pagina de inicio'
   contexto = {
      'title': title
   }
   return render(request, 'taskshtml/saludo.html', contexto)

def signup(request):
   if request.method == 'GET':
      print('enviando formulario')
   else:
      print(request.POST)
      print('obteniendo datos')
      
   form = UserCreationForm
   contexto = {
      'form':form
   }
   return render(request, 'taskshtml/signup.html', contexto)