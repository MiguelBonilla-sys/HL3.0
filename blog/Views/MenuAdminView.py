from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from blog.Models.AuditLogModel import AuditLog

class AdminMenuView(LoginRequiredMixin, TemplateView):
    template_name = 'blog/AdminMenu.html'  # Reemplaza con la ruta correcta

    def get_context_data(self, **kwargs):
        context = super(AdminMenuView, self).get_context_data(**kwargs)
        context['title'] = 'Menu Administrador'
    
        # Obtén los registros de auditoría
        audit_logs = AuditLog.objects.all()

        is_admin = self.request.user.groups.filter(name='Admin').exists() and not self.request.user.groups.filter(name='Staff').exists()

        # Solo añade los registros de auditoría al contexto si el usuario es admin
        if is_admin:
            context['audit_logs'] = audit_logs

        context['is_admin'] = is_admin

        return context