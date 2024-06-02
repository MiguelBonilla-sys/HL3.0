from django.shortcuts import redirect
from django.http import JsonResponse

def login_required_with_token(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login_view')
        
        token = request.COOKIES.get('token')
        if not token:
            return redirect('login_view')

        return view_func(request, *args, **kwargs)
    return _wrapped_view
