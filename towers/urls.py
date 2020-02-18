from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="towers"),
    path('<str:tower_id>/', views.tower, name="tower"),
    
]

