from django.shortcuts import render
from django.http import HttpResponse
from .models import Formulario

# Create your views here.


def index(request):
    if request.method == 'POST':
        error = []
        form = Formulario()
        msg_error = "El campo {0} es Obligatorio"

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
            if Formulario.is_empty(Formulario)==False:
                if Formulario.objects.filter(Cedula=form.Cedula).count() > 0:
                    error.append("La Cedula ya existe")

        form.Sexo = request.POST['Sexo']
        form.Edad = request.POST['Edad']
        if form.Edad == '':
            error.append(msg_error.format("Edad"))

        if 'Casado' in request.POST:
            form.Casado = True
        else:
            form.Casado = False

        if len(error) > 0:
            return render(request, 'form/index.html', {'error_message': error, "form": form})
        else:
            Formulario.Create(form)
            data = Formulario.FindAll(Formulario)
            return render(request, 'form/detail.html', {'form': data, 'success': 'Se ha enviado su formulario con exito '+form.Nombre})
    else:
        return render(request, 'form/index.html')


def detail(request):
    if Formulario.is_empty(Formulario):
        return render(request, 'form/detail.html')
    else:
        data = Formulario.FindAll(Formulario)
        return render(request, 'form/detail.html', {'form': data})


def delete(request):
    if request.method == "POST":
        cedula=request.POST["cedula"]
        Formulario.Remove(Formulario,cedula)
        return HttpResponse(request.POST["cedula"])


def update(request,id):
    if request.method == 'POST':
        error = []
        form = Formulario()
        msg_error = "El campo {0} es Obligatorio"

        form.Nombre = request.POST['Nombre']
        if form.Nombre == '':
            error.append(msg_error.format("Nombre"))

        form.Apellido = request.POST['Apellido']
        if form.Apellido == '':
            error.append(msg_error.format("Apellido"))

        form.Cedula = id

        form.Sexo = request.POST['Sexo']
        form.Edad = request.POST['Edad']
        if form.Edad == '':
            error.append(msg_error.format("Edad"))

        if 'Casado' in request.POST:
            form.Casado = True
        else:
            form.Casado = False

        if len(error) > 0:
            return render(request, 'form/update.html', {'error_message': error, "form": form})
        else:
            Formulario.Update(form.Cedula,form)
            return render(request, 'form/update.html', {'form': form, 'success': 'Se ha actualizado su formulario con exito '+form.Nombre})
    else:
        obj = Formulario.Find(id)[0]
        return render(request, 'form/update.html',{'form':obj})