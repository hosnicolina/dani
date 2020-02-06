from django.contrib import admin

from . import models


@admin.register(models.ManoDeObraDirecta)
class ManoDeObraDirectaAdmin(admin.ModelAdmin):
    pass

@admin.register(models.MaterialesDirectos)
class MaterialesDirectosAdmin(admin.ModelAdmin):
    pass

@admin.register(models.ServiciosDirectos)
class ServiciosDirectosAdmin(admin.ModelAdmin):
    pass

@admin.register(models.MateriaPrima)
class MateriaPrimaAdmin(admin.ModelAdmin):
    pass