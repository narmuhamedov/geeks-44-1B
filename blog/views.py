from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models


# для полной информации
def post_detail_view(request, id):
    if request.method == 'GET':
        post_id = get_object_or_404(models.Post, id=id)
        return render(
            request,
            template_name='post_detail.html',
            context={
                'post_id': post_id
            }
        )




# вывод не полной информации
def post_list_view(request):
    if request.method == "GET":
        # query запрос
        post_object = models.Post.objects.all()
        return render(
            request,
            template_name='post_list.html',
            context={
                'post_object': post_object
            }
        )


def hello_view(request):
    return HttpResponse('Hello World')


def about_view(request):
    return HttpResponse('Меня зовут Радомир мне 27 лет')
