from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="towers"),
    path('<str:tower_id>/', views.tower, name="tower"),
    path('tower/<int:product_id>/', views.detail, name="tower_product"),
]

