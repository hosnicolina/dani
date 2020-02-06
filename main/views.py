from decimal import Decimal

from django.shortcuts import render
from django.db.models import Sum


from costoadmin import models as modeladmin
from costope import models as modelope

# Create your views here.

def dash(request):

    mano_de_obra = modelope.ManoDeObraDirecta.objects.all().aggregate(Sum('salario'))
    materiales = modelope.MaterialesDirectos.objects.all().aggregate(Sum('costo'))
    servicios = modelope.ServiciosDirectos.objects.all().aggregate(Sum('costo'))
    materia_prima = modelope.MateriaPrima.objects.all().aggregate(Sum('costo'))

    total_operativo = mano_de_obra['salario__sum'] + materiales['costo__sum'] + servicios['costo__sum'] + materia_prima['costo__sum']


    mano_de_obra_o = modeladmin.ManoDeObraIndirecta.objects.all().aggregate(Sum('salario'))
    materiales_o = modeladmin.MaterialesIndirectos.objects.all().aggregate(Sum('costo'))
    servicios_o = modeladmin.ServiciosIndirectos.objects.all().aggregate(Sum('costo'))


    total_admistrativo = mano_de_obra_o['salario__sum'] + materiales_o['costo__sum'] + servicios_o['costo__sum']


    total_suma = total_operativo + total_admistrativo

    costo_unitario = total_suma / Decimal(800)

    marge_de_ganancias = costo_unitario * Decimal(0.3)

    kilogramo = costo_unitario +  marge_de_ganancias

    precentacion_500 = kilogramo / 2

    precentacion_250 = precentacion_500 / 2

    ctx = {
        "total_admistrativo":total_admistrativo,
        "total_operativo" : total_operativo,
        "total_suma": total_suma,
        "p_250": precentacion_250,
        "p_500": precentacion_500,
        "costo_unitario":costo_unitario,
        "marge_de_ganancias":marge_de_ganancias,
        "kilogramo":kilogramo
        
    }
    return render(request, "main/boar.html", ctx)