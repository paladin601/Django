from django import forms
from apps.form1.models import Formulario

class Form(forms.ModelForm):
    class Meta:
        model = Formulario

        fields=[
            'Nombre',
            'Apellido',
            'Sexo',
            'Edad',
            'Casado'
        ]
        labels={
            'Nombre' : 'Primer Nombre',
            'Apellido' : 'Primer Apellido',
            'Sexo' : 'Sexo',
            'Edad' : 'Edad',
            'Casado' : 'Eres Casado?'
        }
        
        widgets={
            'Nombre':forms.TextInput(attrs={'class':'form-control'}),
            'Apellido':forms.TextInput(attrs={'class':'form-control'}),
            'Sexo':forms.Select(attrs={'class':'form-control'}),
            'Edad':forms.NumberInput(attrs={'class':'form-control'}),
            'Casado':forms.CheckboxInput(),
        }