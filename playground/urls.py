from django.urls import path
from django.views.generic import TemplateView

from playground import views

urlpatterns = [
    path('http_test/', views.foo),
    path('shit/', TemplateView.as_view())
]
