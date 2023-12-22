from django.http import HttpResponse

# def hola(request):
#     return HttpResponse("hola mundo")
def nombre(request,nombre,apellido):    
    return HttpResponse(f"{apellido},{nombre}")

def fecha_hora(request):
    from datetime import datetime
    ahora = datetime.now().strftime(r"%d/%m%Y %H:%M:%S")
    return HttpResponse(ahora)

def tirar_dado(request):
    import random
    numero = random.randint(1,6)
    if numero == 6:
        return HttpResponse(f"<h1>{numero} Ganaste!</h1>")
    else: return HttpResponse(f"<h1>{numero} perdiste, vuelve a intentar</h1>")
# def index(request): 
#     return render(request,"core/index.hml")