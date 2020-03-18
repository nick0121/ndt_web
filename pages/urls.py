from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('accessories', views.accessories, name="accessories"),
    path('accessory/<query>/', views.accessory, name="accessory"),
    path('accessories/accessory/<int:product_id>/', views.detail, name="accessory_product"),
    path('biminis', views.biminis, name="biminis"),
    path('installation', views.installation, name="installation"),
    path('faq', views.faq, name="faq"),
    path('sitemap', views.sitemap, name="sitemap"),
    path('orders', views.orders, name="orders"),
    path('product', views.product, name="product"),
]