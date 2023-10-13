from django.urls import path
from . import views  # Import views from the current app

urlpatterns = [
    path('hello/', views.hello_django, name='hello_django'),
]
