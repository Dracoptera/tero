from django import forms
from django.forms import ModelForm, TimeField
# .models con punto porque viene de la misma carpeta
from .models import Medicamento, Alarma, Usuario


class TimeInput(forms.TimeInput):
    input_type = "time"


class MedicamentoForm(ModelForm):
    class Meta:
        model = Medicamento
        fields = '__all__'
        # usar lista en vez de __all__ en caso de querer añadir solo algunos en específico.


class AlarmaForm(ModelForm):
    # hora = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))

    class Meta:
        model = Alarma
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["hora"].widget = TimeInput()


class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'
