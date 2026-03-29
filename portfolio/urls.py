from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.projet_list, name='list'),
    path('<int:pk>/', views.projet_detail, name='detail'),
]