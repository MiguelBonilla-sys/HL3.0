from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from blog.Models.AuditLogModel import AuditLog

class AdminMenuView(LoginRequiredMixin, TemplateView):
    """
    Esta es una vista basada en clase para el menú del administrador. 
    Hereda de LoginRequiredMixin y TemplateView para asegurar que el usuario esté autenticado y para manejar la representación de la plantilla, respectivamente.
    """
    template_name = 'blog/AdminMenu.html'  # Define la plantilla que se utilizará para esta vista.

    def get_context_data(self, **kwargs):
        """
        Este método se sobrescribe para añadir datos adicionales al contexto que se pasa a la plantilla.
        """
        context = super(AdminMenuView, self).get_context_data(**kwargs)  # Obtiene el contexto original.
        context['title'] = 'Menu Administrador'  # Añade un título al contexto.
    
        # Obtiene todos los registros de auditoría.
        audit_logs = AuditLog.objects.all()

        # Comprueba si el usuario actual pertenece al grupo 'Admin' y no pertenece al grupo 'Staff'.
        is_admin = self.request.user.groups.filter(name='Admin').exists() and not self.request.user.groups.filter(name='Staff').exists()

        # Si el usuario es un administrador, añade los registros de auditoría al contexto.
        if is_admin:
            context['audit_logs'] = audit_logs

        # Añade la variable is_admin al contexto para poder usarla en la plantilla.
        context['is_admin'] = is_admin

        return context  # Devuelve el contexto actualizado.