from django.shortcuts import render
from django.http import HttpResponse

#fdsf
def hello_view(request):
    return HttpResponse('Hello World')


def about_view(request):
    return HttpResponse('Меня зовут Радомир мне 27 лет')