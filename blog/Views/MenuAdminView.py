from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from blog.Models.AuditLogModel import AuditLog
from django.core.paginator import Paginator

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
        audit_logs = AuditLog.objects.all().select_related('user').order_by('id')  # Usa select_related para optimizar la consulta

        # Transforma los registros de auditoría en una lista de diccionarios, incluyendo el nombre del usuario en lugar del ID
        audit_logs = [
            {
                'id': log.id,
                'timestamp': log.timestamp,
                'user': log.user.username,  # Aquí obtienes el nombre del usuario
                'table_name': log.table_name,
                'change_type': log.change_type,
                'affected_record_id': log.affected_record_id,
                'modified_data': log.modified_data,
            }
            for log in audit_logs
        ]

        # Comprueba si el usuario actual pertenece al grupo 'Admin' y no pertenece al grupo 'Staff'.
        is_admin = self.request.user.groups.filter(name='Admin').exists() and not self.request.user.groups.filter(name='Staff').exists()

        if is_admin:
            paginator = Paginator(audit_logs, 6)  # Crea un paginador con 6 registros por página
            page_number = self.request.GET.get('page')  # Obtiene el número de página de la solicitud GET
            page_obj = paginator.get_page(page_number)  # Obtiene los registros para la página actual
            context['audit_logs'] = page_obj  # Añade los registros de la página actual al contexto
            context['page_obj'] = page_obj  # Añade el objeto de la página al contexto para poder usarlo en la plantilla

        # Añade la variable is_admin al contexto para poder usarla en la plantilla.
        context['is_admin'] = is_admin

        return context  # Devuelve el contexto actualizado.