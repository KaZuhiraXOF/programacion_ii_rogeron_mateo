from django import forms
from nomina.models import Empleado


class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = [
            'cedula',
            'nombres',
            'apellidos',
            'correo',
            'fecha_ingreso',
            'salario_base',
            'estado',
            'departamento',
        ]
        widgets = {
            'cedula': forms.TextInput(attrs={'maxlength': '10', 'placeholder': '10 dígitos'}),
            'fecha_ingreso': forms.DateInput(attrs={'type': 'date'}),
            'salario_base': forms.NumberInput(attrs={'step': '0.01', 'min': '0'}),
        }

    def clean_cedula(self):
        cedula = self.cleaned_data['cedula'].strip()
        if not cedula.isdigit() or len(cedula) != 10:
            raise forms.ValidationError('La cédula debe contener exactamente 10 dígitos numéricos.')
        return cedula

    def clean_salario_base(self):
        salario = self.cleaned_data['salario_base']
        if salario <= 0:
            raise forms.ValidationError('El salario base debe ser mayor a $0.00.')
        return salario