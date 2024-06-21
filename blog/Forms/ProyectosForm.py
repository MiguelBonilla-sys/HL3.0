from django import forms
from django.urls import reverse_lazy
from django.contrib.admin.widgets import AutocompleteSelectMultiple
from blog.Models.ProyectosModel import Proyectos
from blog.Models.IntegrantesModel import Integrantes

class ProyectosForm(forms.ModelForm):
    integrantes_proyecto = forms.ModelMultipleChoiceField(
        queryset=Integrantes.objects.all(),  # Este queryset se puede personalizar en el __init__
        widget=forms.SelectMultiple(attrs={'class': 'select2', 'data-url': reverse_lazy('integrantes-autocomplete')}),
        required=False,
        label="Integrantes"
    )

    class Meta:
        model = Proyectos
        fields = ['nombre_proyecto', 'integrantes_proyecto', 'fecha_proyecto', 'link_proyecto', 'description_proyecto']
        widgets = {
            'fecha_proyecto': forms.DateInput(attrs={'type': 'date'}),
            'link_proyecto': forms.URLInput(attrs={'placeholder': 'https://'}),
            'description_proyecto': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super(ProyectosForm, self).__init__(*args, **kwargs)
        # Personalizar el queryset de integrantes_proyecto si es necesario
        self.fields['integrantes_proyecto'].queryset = Integrantes.objects.filter(estado=True)
        # Establecer valores iniciales para algunos campos, si es necesario
        self.fields['nombre_proyecto'].initial = 'Nombre predeterminado del proyecto'