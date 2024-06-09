# Roles y Permisos en el Proyecto Django

| SuperUser | Funciones |
| --- | --- |
| SuperUser | Agregar, eliminar y modificar parámetros de usuarios |
| /User_Admin | - Visualización de datos cambiados, agregados y eliminados por los "User_Staff", mediante HistorialCambios |

---
## Seccion 2
- Agregar, eliminar y actualizar datos en las siguientes tablas:
  - Cursos
  - Integrantes
  - Noticias
  - Proyectos

```python
class IntegrantesForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['imagen'].required = False
```

```bash
python manage.py runserver
```

Texto random, en el que voy a meter un comando o un mini fragmento de código `\myvenv\Scripts\activate`, y con eso queda resaltado en medio del texto.

Más texto de relleno estilo Lorem Ipsum bla bla bla.

*Negritas*
_cursivas_

/User_Staff
    Funciones:
        - Visualización de datos en las siguientes tablas:
            + Cursos
            + Integrantes
            + Noticias
            + Proyectos
        - Agregar, eliminar y actualizar datos en las mismas tablas mencionadas.