from django.shortcuts import render

def perfil1(request):
    return render(request, 'perfil1.html', {})
def perfil2(request):
    return render(request, 'perfil2.html', {})
def perfil3(request):
    return render(request, 'perfil3.html', {})
