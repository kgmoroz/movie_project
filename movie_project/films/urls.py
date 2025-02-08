from django.urls import path
from .views import add_film, film_list

urlpatterns = [
    path("add/", add_film, name="add_film"),  # Страница добавления фильма
    path("", film_list, name="film_list"),  # Страница списка фильмов
]
