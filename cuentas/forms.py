from django.forms import ModelForm
from .models import Medicamento # .models con punto porque viene de la misma carpeta

class MedicamentoForm(ModelForm):
    class Meta:
        model = Medicamento 
        fields = '__all__'