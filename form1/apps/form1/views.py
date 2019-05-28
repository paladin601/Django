from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from apps.form1.forms import Form
from apps.form1.models import *


def index(request):
    if request.method == 'POST':
        error = []
        form = Formulario()
        msg_error="El campo {0} es Obligatorio"
        form.Nombre = request.POST['Nombre']
        if form.Nombre == '':
            error.append(msg_error.format("Nombre"))

        form.Apellido = request.POST['Apellido']
        if form.Apellido == '':
            error.append(msg_error.format("Apellido"))
             
        form.Cedula = request.POST['Cedula']
        if form.Cedula == '':
            error.append(msg_error.format("Cedula"))
        else:
            if Formulario.objects.count()>0:
                if Formulario.objects.filter(Cedula=form.Cedula).count()>0:
                    error.append("La Cedula ya existe")
        
        form.Sexo = request.POST['Sexo']
        form.Edad = request.POST['Edad']
        if form.Edad == '':
            error.append(msg_error.format("Edad"))

        if 'Casado' in request.POST:
            form.Casado = request.POST['Casado']
            form.Casado = True
        else:
            form.Casado = False

        if len(error) > 0:
            return render(request, 'formulario/index.html', {'error_message': error, "form": form})
        else:
            form.save()
            data = Formulario.objects.all()
            return render(request, 'formulario/detail.html', {'form': data , 'success':'Se ha enviado su formulario con exito '+form.Nombre})
    else:
        form = Form()
        return render(request, 'formulario/index.html')


def detail(request):
    if Formulario.objects.count()>0:
        form = Formulario.objects.all()
        return render(request, 'formulario/detail.html', {'form': form})
    else:
        return render(request, 'formulario/detail.html')

def delete(request):
    if request.method == 'POST':
        Formulario.delete(request.POST['cedula'])
        return HttpResponse(request.POST['cedula'])

def update(request,id):
    if request.method == 'POST':
        error = []
        form = Formulario()
        msg_error="El campo {0} es Obligatorio"
        form.Nombre = request.POST['Nombre']
        if form.Nombre == '':
            error.append(msg_error.format("Nombre"))

        form.Apellido = request.POST['Apellido']
        if form.Apellido == '':
            error.append(msg_error.format("Apellido"))
        form.Cedula=id
        form.Sexo = request.POST['Sexo']
        form.Edad = request.POST['Edad']
        if form.Edad == '':
            error.append(msg_error.format("Edad"))

        if 'Casado' in request.POST:
            form.Casado = request.POST['Casado']
            form.Casado = True
        else:
            form.Casado = False

        if len(error) > 0:
            return render(request, 'formulario/update.html', {'error_message': error, "form": form})
        else:
            Formulario.Update(id,form)
            return render(request, 'formulario/update.html', {'form': form , 'success':'Se ha Editado su formulario con exito '})
    else:
        obj=Formulario.Find(id)[0]
        return render(request, 'formulario/update.html',{'form':obj})

