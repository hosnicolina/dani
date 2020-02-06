from decimal import Decimal
from django.shortcuts import render
from django.db.models import Sum
from django.urls import reverse_lazy

from django.views.generic import CreateView


from . import models

# Create your views here.


def admin(request):

    mano_de_obra = models.ManoDeObraDirecta.objects.all()
    materiales = models.MaterialesDirectos.objects.all()
    servicios = models.ServiciosDirectos.objects.all()
    materia_prima = models.MateriaPrima.objects.all()

    total = mano_de_obra.aggregate(Sum('salario'))['salario__sum']
    total_materiales = materiales.aggregate(Sum('costo'))['costo__sum']
    total_servicios = servicios.aggregate(Sum('costo'))['costo__sum']
    total_prima = materia_prima.aggregate(Sum('costo'))['costo__sum']

    costos = []
    total_completo = Decimal(0)

    costos.append(total)
    costos.append(total_materiales)
    costos.append(total_servicios)
    costos.append(total_prima)


    for costo in costos:
        if costo != None:
            total_completo = total_completo + costo

    print(type(Decimal(0)))
    ctx = {
        "mano": mano_de_obra,
        "materiales": materiales,
        "servicios": servicios,
        "materia_prima": materia_prima,
        "total": total,
        "total_prima": total_prima,
        "total_materiales": total_materiales,
        "total_servicios": total_servicios,
        "total_completo": total_completo
    }

    return render(request, "costope/admin.html", ctx)


class MaterialesCreateView(CreateView):
    template_name = "costope/material_form.html"
    model = models.MateriaPrima
    fields = ['materia', 'cantidad', 'costo']
    success_url = reverse_lazy('operativos:costo-operativos')

class ManodeObraCreateView(CreateView):
    template_name = "costope/mano_de_obra_form.html"
    model = models.ManoDeObraDirecta
    fields = ['cargo', 'cantidad', 'salario']
    success_url = reverse_lazy('operativos:costo-operativos')

class MaterialesDirectoCreateView(CreateView):
    template_name = "costope/materiales_directos_form.html"
    model = models.MaterialesDirectos
    fields = [ 'material', 'costo' ]
    success_url = reverse_lazy('operativos:costo-operativos')

class ServiciosDirectoCreateView(CreateView):
    template_name = "costope/servicios_directos_form.html"
    model = models.ServiciosDirectos
    fields = [ 'servicio', 'costo' ]
    success_url = reverse_lazy('operativos:costo-operativos')
