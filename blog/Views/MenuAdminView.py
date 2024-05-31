from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

class AdminMenuView(LoginRequiredMixin, TemplateView):
    template_name = 'blog/adminmenu.html'  # Reemplaza con la ruta correcta

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Menu Administrador'
        return context

