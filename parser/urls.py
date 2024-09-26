from django.urls import path
from . import views

urlpatterns = [
    path('manas_films_list/', views.ManasFilListView.as_view(), name='manas_film_list'),
    path('start_parser/', views.ParserFormView.as_view()),
]
