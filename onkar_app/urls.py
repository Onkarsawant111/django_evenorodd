from django.urls import path
from onkar_app import views

urlpatterns = [
    path('', views.onkar),
    path('evenodd', views.evenodd),
]
