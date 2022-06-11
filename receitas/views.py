from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404

from receitas.models import People


def index(request: HttpRequest):
    return render(request, 'index.html')


def album(request: HttpRequest):
    nomes = People.objects.all()
    dados: dict = {'Lovecraftianos': nomes}
    return render(request, 'album/index.html', dados)


def view(request: HttpRequest, people_id):
    people = get_object_or_404(People, pk=people_id)
    dado: dict = {'people': people}
    return render(request, 'album/view.html', dado)
