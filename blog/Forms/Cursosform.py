from django.forms import ModelForm
from  blog.Models.CursosModel import Cursos

class CursosForm(ModelForm):
    class Meta:
        model = Cursos
        fields = ['nombre_curso', 'fechainicial_curso', 'fechafinal_curso', 'link_curso', 'descripcion_curso']