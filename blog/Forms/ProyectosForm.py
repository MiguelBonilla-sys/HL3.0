from django import forms
from django.urls import reverse_lazy
from blog.Models.ProyectosModel import Proyectos
from blog.Models.IntegrantesModel import Integrantes
from blog.Models.ProyectosIntegrantesModel import ProyectosIntegrantesProyecto

class ProyectosForm(forms.ModelForm):
    integrantes = forms.ModelMultipleChoiceField(
        queryset=Integrantes.objects.filter(estado=True),
        widget=forms.SelectMultiple(attrs={'class': 'select2', 'data-url': reverse_lazy('integrantes-autocomplete')}),
        required=False,
        label="Integrantes"
    )

    class Meta:
        model = Proyectos
        fields = ['nombre_proyecto', 'fecha_proyecto', 'link_proyecto', 'description_proyecto']
        widgets = {
            'fecha_proyecto': forms.DateInput(attrs={'type': 'date'}),
            'link_proyecto': forms.URLInput(attrs={'placeholder': 'https://'}),
            'description_proyecto': forms.Textarea(attrs={'rows': 3}),
        }

    def save(self, commit=True):
        proyecto = super(ProyectosForm, self).save(commit=False)
        if commit:
            proyecto.save()
            self.save_m2m()
        return proyecto

    def save_m2m(self):
        try:
            integrantes_seleccionados = self.cleaned_data.get('integrantes')
            ProyectosIntegrantesProyecto.objects.filter(proyectos=self.instance).delete()  # Limpia la relación existente
            for integrante in integrantes_seleccionados:
                ProyectosIntegrantesProyecto.objects.create(proyectos=self.instance, integrantes=integrante)
        except Exception as e:
            print(f"Error al guardar integrantes en el proyecto: {e}")