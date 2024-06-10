from django import forms
from blog.Models.NoticiasModel import Noticias

class NoticiasForm(forms.ModelForm):
    class Meta:
        model = Noticias
        fields = ['nombre_noticia', 'fecha_noticia', 'link_noticia', 'description_noticia']