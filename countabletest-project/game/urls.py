from django.urls import path
from . import views

urlpatterns = [
    path('create', views.create, name='create'),
    path('savemove', views.savemove, name='savemove'),
    path('<int:game_id>/', views.detail, name='detail'),
]
