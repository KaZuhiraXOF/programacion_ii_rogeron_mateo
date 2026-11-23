from django import forms
from nomina.models import Departamento


class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ['codigo', 'nombre', 'ubicacion']
        widgets = {
            'codigo': forms.TextInput(attrs={'placeholder': 'Ej. DEP-TI'}),
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre del departamento'}),
            'ubicacion': forms.TextInput(attrs={'placeholder': 'Piso / Ala'}),
        }

    def clean_codigo(self):
        codigo = self.cleaned_data['codigo'].strip().upper()
        if len(codigo) < 3:
            raise forms.ValidationError('El código debe tener al menos 3 caracteres.')
        return codigo