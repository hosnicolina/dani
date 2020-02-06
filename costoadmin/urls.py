from django.urls import path
from . import views

app_name = "administrativo"
urlpatterns = [
    path('administrativo/', views.admin, name="costo-admin"),
    path('administrativo/mano-add', views.ManoDeObraIndirectaCreateView.as_view(), name="mano"),
    path('administrativo/mate-add', views.MaterialesIndirectosCreateView.as_view(), name="materiales"),
    path('administrativo/servi-add', views.ServiciosIndirectosCreateView.as_view(), name="servicios"),
]
