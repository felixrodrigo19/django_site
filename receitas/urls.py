from django.urls import path

from receitas import views

urlpatterns = [
    path('', views.index, name='index'),
    path('album', views.album, name='album'),
    path('<int:people_id>', views.view, name='view_people')
]
