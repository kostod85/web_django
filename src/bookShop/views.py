from django.shortcuts import render, HttpResponse
from random import randint

# Create your views here.
names = ('Антон', 'Семен','Максим')

def hello_world_views(request):
    name = names[randint(0, 2)]
    print(request.user)
    return HttpResponse(f"<h1> Hello {request.user or name} </h1>")