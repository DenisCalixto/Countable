from django.urls import path
from . import views

urlpatterns = [
    path('create', views.create, name='create'),
    path('saveimagemove', views.saveimagemove, name='saveimagemove'),
    path('<int:game_id>/', views.detail, name='detail'),
]
