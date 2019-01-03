from django.urls import path

from . import views

app_name = 'health'
urlpatterns = [
    path('', views.home, name='home'),
    path('<str:symptom>/', views.diagnoses, name='diagnoses'),
]
