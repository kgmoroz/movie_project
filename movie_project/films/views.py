from django.shortcuts import render, redirect
from .models import Film
from .forms import FilmForm

def add_film(request):
    if request.method == "POST":
        form = FilmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("film_list")  # Перенаправление на страницу со списком фильмов
    else:
        form = FilmForm()

    return render(request, "films/add_film.html", {"form": form})

def film_list(request):
    films = Film.objects.all()  # Получаем все фильмы из базы данных
    return render(request, "films/film_list.html", {"films": films})
