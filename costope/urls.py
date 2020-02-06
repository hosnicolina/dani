from django.urls import path
from . import views

app_name = "operativos"
urlpatterns = [
    path('operativos/', views.admin, name="costo-operativos"),
    path('operativos/materia-add/', views.MaterialesCreateView.as_view() , name="materia"),
    path('operativos/mano-add/', views.ManodeObraCreateView.as_view() , name="mano"),
    path('operativos/materiales-add/', views.MaterialesDirectoCreateView.as_view() , name="material"),
    path('operativos/servicios-add/', views.ServiciosDirectoCreateView.as_view() , name="servicios"),
]
