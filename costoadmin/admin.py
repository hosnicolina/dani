from django.contrib import admin

from . import models


@admin.register(models.ManoDeObraIndirecta)
class ManoDeObraIndirectaAdmin(admin.ModelAdmin):
    pass

@admin.register(models.MaterialesIndirectos)
class MaterialesIndirectosAdmin(admin.ModelAdmin):
    pass

@admin.register(models.ServiciosIndirectos)
class ServiciosIndirectosAdmin(admin.ModelAdmin):
    pass