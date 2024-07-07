from django import forms
from blog.Models.NoticiasModel import Noticias
import base64

class NoticiasForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['imagen_noticia'].required = False

    class Meta:
        model = Noticias
        fields = ['nombre_noticia', 'fecha_noticia', 'link_noticia', 'description_noticia', 'fuente', 'imagen_noticia']

    
    def clean_imagen_noticia(self):
        imagen_noticia = self.cleaned_data.get('imagen_noticia')

        # Verificar si imagen_noticia es un archivo
        if hasattr(imagen_noticia, 'read'):
            # Convertir la imagen a base64
            imagen_data = imagen_noticia.read()
            base64_encoded = base64.b64encode(imagen_data).decode()

            # Asignar la imagen en base64 al campo imagen_noticia del modelo
            self.cleaned_data['imagen_noticia'] = base64_encoded
            return base64_encoded
        else:
            # Si imagen_noticia ya es una cadena base64, simplemente retornarla
            return imagen_noticia
    