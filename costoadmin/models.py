from django.db import models
from djmoney.models.fields import MoneyField

class ManoDeObraIndirecta(models.Model):
    # cargo
    # cantidad
    # salario
    # creacion
    # actualizacion
    cargo = models.CharField("Cargo", max_length=50, blank=False, null=False)
    cantidad = models.IntegerField("Cantidad", default=1)
    salario = MoneyField(max_digits=19, decimal_places=2, default_currency='BSS')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.cargo} - {self.salario}'

    def save(self, *args, **kwargs):
        if self.cantidad > 1:
            self.salario =  self.salario * self.cantidad
        super().save(*args, **kwargs)
    


class MaterialesIndirectos(models.Model):
    # materiales
    # costo
    # creacion
    # actualizacion
    material = models.CharField("Material", max_length=50, blank=False, null=False)
    costo = MoneyField(max_digits=19, decimal_places=2, default_currency='BSS')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.material} - {self.costo}'


class ServiciosIndirectos(models.Model):


    servicio = models.CharField("Servicio", max_length=50, blank=False, null=False)
    costo = MoneyField(max_digits=19, decimal_places=2, default_currency='BSS')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.servicio} - {self.costo}'
    
