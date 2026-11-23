from django import forms
from nomina.models import RolPago


class RolPagoForm(forms.ModelForm):
    class Meta:
        model = RolPago
        fields = ['empleado', 'periodo_inicio', 'periodo_fin', 'conceptos', 'estado_pago']
        widgets = {
            'periodo_inicio': forms.DateInput(attrs={'type': 'date'}),
            'periodo_fin': forms.DateInput(attrs={'type': 'date'}),
            'conceptos': forms.CheckboxSelectMultiple(),
        }

    def clean(self):
        cleaned_data = super().clean()
        inicio = cleaned_data.get('periodo_inicio')
        fin = cleaned_data.get('periodo_fin')
        if inicio and fin and fin < inicio:
            self.add_error('periodo_fin', 'La fecha de fin no puede ser anterior a la fecha de inicio.')
        return cleaned_data