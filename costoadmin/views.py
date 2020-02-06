from decimal import Decimal

from django.shortcuts import render
from django.db.models import Sum

from django.urls import reverse_lazy

from django.views.generic import CreateView


from . import models

# Create your views here.

def total_o_cero(total):
    if total == None:
        return Decimal(0)
    return total


def admin(request):

    mano_de_obra = models.ManoDeObraIndirecta.objects.all()
    materiales = models.MaterialesIndirectos.objects.all()
    servicios = models.ServiciosIndirectos.objects.all()

    total = total_o_cero( mano_de_obra.aggregate(Sum('salario'))['salario__sum'] ) 
    total_materiales = total_o_cero( materiales.aggregate(Sum('costo'))['costo__sum'] ) 
    total_servicios = total_o_cero( servicios.aggregate(Sum('costo'))['costo__sum'] ) 

    costos = []

    total_completo = Decimal(0)

    costos.append(total)
    costos.append(total_materiales)
    costos.append(total_servicios)

    for costo in costos:
        if costo != None:
            total_completo = costo + total_completo

    ctx = {
        "mano":mano_de_obra,
        "materiales": materiales,
        "servicios": servicios,
        "total": total,
        "total_materiales": total_materiales,
        "total_servicios": total_servicios,
        "total_completo":total_completo
    }

    return render(request, "costoadmin/admin.html", ctx)

class ManoDeObraIndirectaCreateView(CreateView):
    template_name = "costoadmin/form.html"
    extra_context = { "title" : "Mano De Obra Indirecta" }
    model = models.ManoDeObraIndirecta
    fields = ['cargo', 'cantidad', 'salario']
    success_url = reverse_lazy('administrativo:costo-admin')

class MaterialesIndirectosCreateView(CreateView):
    template_name = "costoadmin/form.html"
    extra_context = { "title" : "Materiales Indirectos" }
    model = models.MaterialesIndirectos
    fields = ['material', 'costo']
    success_url = reverse_lazy('administrativo:costo-admin')

class ServiciosIndirectosCreateView(CreateView):
    template_name = "costoadmin/form.html"
    extra_context = { "title" : "Servicios Indirectos" }
    model = models.ServiciosIndirectos
    fields = [ 'servicio', 'costo' ]
    success_url = reverse_lazy('administrativo:costo-admin')

