from django.shortcuts import render
from django.http import HttpResponse
from .models import Film


def wszystkie_filmy(request):
    # return HttpResponse("<h1>To jest nasz pierwszy test</h1>")
    # test = "to jest cos we views"
    # return render(request, 'filmy.html', {'text': test})
    # test = ["Avatar" "Titanic"]
    # return render(request, 'filmy.html', ["Avatar" "Titanic"])
    wszystkie = Film.objects.all()
    return render(request, 'filmy.html', {'filmy' : wszystkie})