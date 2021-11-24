from django.contrib import admin
from app_principal.models import Usuario, Contrato, Aliado, Companero_Equipo, Persona_Salvada, Hecho, Enemigo, Mision

# Register your models here.


class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("dni_usuario", "nombres_usuario", "apellidos_usuario")


class ContratoAdmin(admin.ModelAdmin):
    list_display = ("usuario", "ref_contrato", "nombre_patrocinador",
                    "inicio_contrato", "fin_contrato", "ganancia_por_contrato")


class AliadoAdmin(admin.ModelAdmin):
    list_display = ("usuario", "nombre_aliado",
                    "idioma_aliado", "es_extraterrestre_aliado")


class CompaneroAdmin(admin.ModelAdmin):
    list_display = ("usuario", "nombre_companero", "telefono_companero",
                    "email_companero", "cumpleanos_companero")


class PersonaAdmin(admin.ModelAdmin):
    list_display = ("id_persona", "nombre_persona_salvada",
                    "edad_persona_salvada")


class HechoAdmin(admin.ModelAdmin):
    list_display = ("usuario", "persona", "lugar_hecho",
                    "fecha_hecho", "descripcion_hecho")


class EnemigoAdmin(admin.ModelAdmin):
    list_display = ("usuario", "alias_enemigo", "nombre_real_enemigo",
                    "habilidad_principal_enemigo", "es_extraterrestre_enemigo")


class MisionAdmin(admin.ModelAdmin):
    list_display = ("usuario", "codigo", "nombre_mision", "fecha",
                    "estado", "observaciones")


admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Contrato, ContratoAdmin)
admin.site.register(Aliado, AliadoAdmin)
admin.site.register(Companero_Equipo, CompaneroAdmin)
admin.site.register(Persona_Salvada, PersonaAdmin)
admin.site.register(Hecho, HechoAdmin)
admin.site.register(Enemigo, EnemigoAdmin)
admin.site.register(Mision, MisionAdmin)
