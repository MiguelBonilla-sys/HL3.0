from django import forms
from blog.Models.ProyectosModel import Proyectos

class ProyectosForm(forms.ModelForm):
    class Meta:
        model = Proyectos
        fields = ['nombre_proyecto', 'intengrantes_proyecto', 'fecha_proyecto', 'link_proyecto', 'description_proyecto']