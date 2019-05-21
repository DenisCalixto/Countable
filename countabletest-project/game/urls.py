from django.urls import path
from . import views

urlpatterns = [
    path('create', views.create, name='create'),
    path('<int:game_id>/', views.detail, name='detail'),
    path('<int:game_id>/savemove', views.savemove, name='savemove'),
]
