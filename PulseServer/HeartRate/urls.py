from django.urls import path
from django.views.generic import TemplateView

from HeartRate import views

app_name = 'HeartRate'

urlpatterns = [
    path('create/', views.create),
    path('update/', views.update),
    path('get/', views.get)
]
