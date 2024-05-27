from django.forms import ModelForm
from  blog.Models.ProyectosModel import Proyectos

class ProyectosForm(ModelForm):
    class Meta:
        model = Proyectos
        fields = ['idproyectos', 'nombre_proyecto', 'intengrantes_proyecto', 'fecha_proyecto', 'link_proyecto', 'description_proyecto', 'historial_cambios_idhistorial_cambios']