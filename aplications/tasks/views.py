from email import message
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.

def inicio(request):
   title = 'pagina de inicio'
   contexto = {
      'title': title
   }
   return render(request, 'taskshtml/saludo.html', contexto)


class RegistroUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']


class registro(View):  
   
    def get(self, request):
       contexto = {
          'form':RegistroUserForm()
          }
       return render(request, "taskshtml/registro.html", contexto)
    
    def post(self, request):
        #form=UserCreationForm(request.POST)
        form = RegistroUserForm(request.POST)    
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('inicio')
        else:
            contexto = {
               'form':RegistroUserForm(request.POST) 
               }
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])      
        return render(request, "taskshtml/signup.html", contexto)

def cerrarSesion(request):
    logout(request)
    return redirect('inicio')

def logear(request):
   if request.method=="POST": #si se pulsa el boton de login
      form = AuthenticationForm(request, data=request.POST)
      if form.is_valid():
         nombre_usuario = form.cleaned_data.get("username")
         passwo = form.cleaned_data.get("password")
         usuario = authenticate(username=nombre_usuario, password=passwo)
         if usuario is not None:
            login(request, usuario)
            return redirect("inicio")
         else:
            messages.error(request, "Usuario no valido")
      else:
         messages.error(request, "Informacion incorrecta")
         
   contexto = {
               'form':AuthenticationForm()
               }
   return render(request, "taskshtml/login.html", contexto)


