from django.forms import ModelForm
from .models import Medicamento # .models con punto porque viene de la misma carpeta

class MedicamentoForm(ModelForm):
    class Meta:
        model = Medicamento 
        fields = '__all__'
        # usar lista en vez de __all__ en caso de querer añadir solo algunos en específico.