from django.db import models
from djmoney.models.fields import MoneyField


class MateriaPrima(models.Model):
    materia = models.CharField("Materia", max_length=150, blank=False, null=False)
    cantidad = models.IntegerField("Cantidad", default=1)
    costo =  MoneyField(max_digits=19, decimal_places=2, default_currency='BSS')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.materia} - {self.costo}'

class ManoDeObraDirecta(models.Model):
    # cargo
    # cantidad
    # salario
    # creacion
    # actualizacion
    cargo = models.CharField("Cargo", max_length=150, blank=False, null=False)
    cantidad = models.IntegerField("Cantidad", default=1)
    salario = MoneyField(max_digits=19, decimal_places=2, default_currency='BSS')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.cantidad > 1:
            self.salario =  self.salario * self.cantidad
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.cargo} - {self.salario}'
    


class MaterialesDirectos(models.Model):
    # materiales
    # costo
    # creacion
    # actualizacion
    material = models.CharField("Material", max_length=150, blank=False, null=False)
    costo = MoneyField(max_digits=19, decimal_places=2, default_currency='BSS')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.material} - {self.costo}'


class ServiciosDirectos(models.Model):
    # servicio
    # costo
    # creacion
    # actualizacion
    servicio = models.CharField("Servicio", max_length=150, blank=False, null=False)
    costo = MoneyField(max_digits=19, decimal_places=2, default_currency='BSS')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.servicio} - {self.costo}'
    
