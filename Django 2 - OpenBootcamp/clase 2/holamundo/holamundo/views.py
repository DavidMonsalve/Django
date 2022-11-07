from django.http import HttpResponse

def adulto(request, edad):
    if edad >= 18:
        return HttpResponse("Eres mayor de edad.")

    else:
        return HttpResponse("No eres mayor de edad.")