from django import forms
from app_principal.models import Usuario, Contrato, Aliado, Companero_Equipo, Persona_Salvada, Hecho, Enemigo, Mision


class AgregarUsuariosForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['dni_usuario', 'nombres_usuario',
                  'apellidos_usuario', ]


class AgregarAliadosForm(forms.ModelForm):
    class Meta:
        model = Aliado
        fields = ['usuario', 'nombre_aliado',
                  'idioma_aliado', 'es_extraterrestre_aliado', ]
    # def __init__(self,*args,**kwargs):
     #   super().__init__(*args,**kwargs)
      #  for field in iter(self.fields):
       #     self.fields[field].widget.attrs.update({'class':'form-control'})


class AgregarCompanerosForm(forms.ModelForm):
    class Meta:
        model = Companero_Equipo
        fields = ['usuario', 'nombre_companero',
                  'telefono_companero', 'email_companero', 'cumpleanos_companero', ]


class AgregarEnemigosForm(forms.ModelForm):
    class Meta:
        model = Enemigo
        fields = ['usuario', 'alias_enemigo',
                  'nombre_real_enemigo', 'habilidad_principal_enemigo', 'es_extraterrestre_enemigo', ]


class AgregarHechosForm(forms.ModelForm):
    class Meta:
        model = Hecho
        fields = ['usuario', 'persona',
                  'lugar_hecho', 'fecha_hecho', 'descripcion_hecho', ]


class AgregarSalvadosForm(forms.ModelForm):
    class Meta:
        model = Persona_Salvada
        fields = ['id_persona', 'nombre_persona_salvada',
                  'edad_persona_salvada', ]


class AgregarMisionesForm(forms.ModelForm):
    class Meta:
        model = Mision
        fields = ['usuario', 'codigo',
                  'nombre_mision', 'fecha', 'estado', 'observaciones', ]


class AgregarContratosForm(forms.ModelForm):
    class Meta:
        model = Contrato
        fields = ['usuario', 'ref_contrato',
                  'nombre_patrocinador', 'inicio_contrato', 'fin_contrato', 'ganancia_por_contrato', ]
