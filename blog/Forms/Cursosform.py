from django.forms import ModelForm
from  blog.Models.CursosModel import Cursos

class CursosForm(ModelForm):
    class Meta:
        model = Cursos
        fields = ['nombre_curso', 'fechainicial_curso', 'fechafina_cursol', 'link_curso', 'descripcion_cursol']
