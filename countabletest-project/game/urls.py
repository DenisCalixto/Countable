from django.urls import path
from . import views

urlpatterns = [
    path('<int:game_id>/', views.detail, name='detail'),
]