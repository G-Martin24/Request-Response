# django-request-response
Este proyecto es una actividad de ejemplo para demostrar el manejo de solicitudes (requests) y respuestas (responses) en el framework Django de Python.
## Instrucciones de Ejecución

Para ejecutar este proyecto localmente, sigue estos pasos:

1. **Clona el repositorio:**
   ```bash
   git clone [https://github.com/TuUsuario/django-request-response.git](https://github.com/TuUsuario/django-request-response.git)
   cd django-request-response
   ```
   (Reemplaza `TuUsuario/django-request-response.git` con la URL de tu repositorio).

2. **Crea y activa un entorno virtual (si no lo hiciste localmente):**
   ```bash
   python -m venv env
   source env/bin/activate  # En Linux/macOS
   .\env\Scripts\activate  # En Windows
   ```

3. **Instala las dependencias (Django):**
   ```bash
   pip install django
   ```

4. **Ejecuta el servidor de desarrollo:**
   ```bash
   python manage.py runserver
   ```

5. **Abre tu navegador web y ve a:** `http://127.0.0.1:8000/request/` para ver la aplicación en funcionamiento.

## Funcionalidades Demostradas

Este proyecto incluye ejemplos de:

* Obtener el User-Agent del request.
* Acceder a otros atributos del request.
* Implementación de un middleware simple.
* Uso de QueryDict para parámetros en la URL.
* Devolución de diferentes tipos de respuestas HTTP (`HttpResponse`, `HttpResponseNotFound`, `JsonResponse`, `StreamingHttpResponse`, `FileResponse`).
* Añadir headers a la respuesta HTTP.
* Verificar si la conexión es segura (HTTPS).
* Una vista de "Home" básica.

 ## Estructura del Proyecto
 ejercicio1/          # Carpeta principal del proyecto Django
├── manage.py
├── ejercicio1/      # Carpeta del proyecto Django (configuración)
│   ├── init.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py      # URLs principales del proyecto
│   └── wsgi.py
└── request/         # Tu aplicación 'request'
├── init.py
├── templates/
│   └── request/
│       └── index.html # Tu template principal
├── urls.py      # URLs de la aplicación 'request'
└── views.py     # Lógica de las vistas
env/               # Entorno virtual (debería estar ignorado por .gitignore)
README.md
.gitignore
db.sqlite3          # Base de datos (debería estar ignorada)
