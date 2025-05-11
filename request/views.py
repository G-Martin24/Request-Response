from django.http import (
    HttpResponse,
    HttpResponseNotFound,
    JsonResponse,
    StreamingHttpResponse,
    FileResponse
)

from django.shortcuts import render

def index(request):
    return render(request, 'request/index.html')

def request_example(request):
    return HttpResponse(f"User-Agent: {request.headers.get('User-Agent')}")

def app_attributes_example(request):
    texto = f"Path: {request.path}<br>Method: {request.method}<br>Encoding: {request.encoding}"
    return HttpResponse(texto)

def middleware_example(request):
    return HttpResponse("Ejemplo de middleware (sin lógica adicional)")

def querydict_example(request):
    nombre = request.GET.get('nombre', 'invitado')
    return HttpResponse(f"Hola {nombre}")

def response_example(request):
    return HttpResponse("Esta es una respuesta directa.")

def response_subclasses_example(request):
    return HttpResponseNotFound("Página no encontrada (404)")

def json_response_example(request):
    data = {"mensaje": "Hola, JSON!", "estado": "ok"}
    return JsonResponse(data)

def stream_response_example(request):
    def generador():
        yield "Primera línea\n"
        yield "Segunda línea\n"
        yield "Tercera línea\n"
    return StreamingHttpResponse(generador())

def file_response_example(request):
    # Asegurate de tener un archivo llamado ejemplo.txt en la raíz del proyecto
    return FileResponse(open('ejemplo.txt', 'rb'), as_attachment=True)

def response_base_example(request):
    response = HttpResponse("Contenido personalizado")
    response['X-Custom-Header'] = 'Valor'
    return response

def is_secure_example(request):
    seguro = request.is_secure()
    return HttpResponse(f"¿La conexión es segura? {seguro}")

def home_view(request):
    return HttpResponse("Bienvenido a la Home Page")
