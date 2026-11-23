from django import forms
from nomina.models import ConceptoSalarial


class ConceptoSalarialForm(forms.ModelForm):
    class Meta:
        model = ConceptoSalarial
        fields = ['nombre', 'tipo', 'monto_fijo', 'es_recurrente']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Ej. Bono de Transporte'}),
            'monto_fijo': forms.NumberInput(attrs={'step': '0.01', 'min': '0.01'}),
        }

    def clean_monto_fijo(self):
        monto = self.cleaned_data['monto_fijo']
        if monto <= 0:
            raise forms.ValidationError('El monto fijo debe ser mayor a $0.00.')
        return monto