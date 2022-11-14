from django.shortcuts import render
from django.http import HttpResponse
from .models import Comment

# Create your views here.
def test(request):
    return HttpResponse("Funciona")

def create(request):
    # comment = Comment(name = "David", score = 5, comment = "esto es un comment")
    # comment.save()

    comment = Comment.objects.create(name = "alex")
    return HttpResponse("creado")

def delete(request):
    #comment = Comment.objects.get(id = 1)
    #comment.delete()
    Comment.objects.filter(id=2).delete()
    return HttpResponse("ruta para probar los datos borrados")