from django.urls import path
from . import views

urlpatterns = [
    path('available', views.available, name='available'),
    path('post/', views.post, name='post'),
]
