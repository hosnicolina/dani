from django.forms import ModelForm

from . import models

class MateriaPrimaForm(ModelForm):
    class Meta:
        model = models.MateriaPrima
        fields = ['materia', 'cantidad', 'costo']
