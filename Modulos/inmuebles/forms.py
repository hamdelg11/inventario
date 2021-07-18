from django import forms
from django.forms import widgets
from .models import Empleado, Producto

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombres','apellidos','cargo']
        labels = {
            'nombres': 'Nombre(s) del empleado:',
            'apellidos': 'Apellidos del empleado:',
            'cargo': 'Cargo del empleado:'
        }
        widgets = {
            'nombres': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'apellidos': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'cargo': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            )

        }

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['cuenta','concepto',
        'fecha_de_adquisicion', 'factura_o_donacion',
         'proveedor', 'inventario_o_codigo_del_activo',
         'descripcion', 'marca', 'serie','costo_de_adquisicion',
         'clasificacion', 'responsable', 'estado_fisico',
         'ubicacion', 'observaciones']
        labels = {
            'cuenta': 'Cuenta:',
            'concepto': 'Concepto:',
            'fecha_de_adquisicion': 'Fecha de adquisicion:',
            'factura_o_donacion': 'Factura o donacion:',
            'proveedor': 'Proveedor:',
            'inventario_o_codigo_del_activo': 'Inventario o codigo del activo:',
            'descripcion': 'Descripcion:',
            'marca': 'Marca:',
            'serie': 'Serie:',
            'costo_de_adquisicion': 'Costo de adquisicion:',
            'clasificacion': 'Clasificacion:',
            'responsable': 'Responsable:',
            'estado_fisico': 'Estado fisico:',
            'ubicacion': 'Ubicacion:',
            'observaciones': 'Observaciones:'
         }
        widgets= {

            'cuenta': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'concepto': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'fecha_de_adquisicion': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'dd/mm/aa'
                }
            ),

            'factura_o_donacion': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'proveedor': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'inventario_o_codigo_del_activo': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'descripcion': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),

            'marca': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'serie': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'costo_de_adquisicion': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'mayor o igual a 0'
                }
            ),

            'clasificacion': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'responsable': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),

            'estado_fisico': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),

            'ubicacion': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'observaciones': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),


         }
