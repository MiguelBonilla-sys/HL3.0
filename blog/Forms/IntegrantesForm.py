from django.forms import ModelForm
from blog.Models.IntegrantesModel import Integrantes
import base64

class IntegrantesForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['imagen'].required = False

    class Meta:
        model = Integrantes
        fields = ['nombre_integrante', 'semestre', 'correo', 'link_git', 'imagen', 'estado']

    def clean_imagen(self):
        imagen = self.cleaned_data.get('imagen')
    
        if imagen:
            # Convertir la imagen a base64
            imagen_data = imagen.read()
            base64_encoded = base64.b64encode(imagen_data).decode()
    
            # Asignar la imagen en base64 al campo imagen del modelo
            self.cleaned_data['imagen'] = base64_encoded
            return base64_encoded
        return imagen