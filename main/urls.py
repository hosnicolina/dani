from django.urls import path
from . import views

app_name = "dash"
urlpatterns = [
    path('', views.dash, name="boar"),
]
