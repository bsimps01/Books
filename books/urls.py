from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home),
    path('book/<int:book_id>', views.detail, name='detail')
]