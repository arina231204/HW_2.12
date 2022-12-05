from django.urls import path
from . import views

urlpatterns = [
    path('greetings/', views.greetings, name='greetings'),
    path('', views.list_item, name='list_item'),
    path('shop/<int:id>/', views.detail_item, name='detail'),
    ]