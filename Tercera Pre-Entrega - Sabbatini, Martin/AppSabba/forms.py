from django import forms


#creamos a partir del model
class CursoFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    comision = forms.IntegerField()


class EstudianteFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField()