from django.db import models


# Create your models here.


class Usuario(models.Model):
    dni_usuario = models.PositiveIntegerField(
        primary_key=True, verbose_name="ID Usuario", help_text="")
    nombres_usuario = models.CharField(
        max_length=30, verbose_name="Nombres", help_text="")
    apellidos_usuario = models.CharField(
        max_length=30, verbose_name="Apellidos", help_text="")

    def __str__(self):
        return f'{self.nombres_usuario} {self.apellidos_usuario}'


class Aliado(models.Model):
    usuario = models.ForeignKey(
        Usuario, on_delete=models.CASCADE, verbose_name="Aliado de")
    nombre_aliado = models.CharField(
        primary_key=True, max_length=30, verbose_name="Nombre", help_text="")
    idioma_aliado = models.CharField(max_length=20, verbose_name="Idioma",
                                     blank=True, null=True, help_text="")
    es_extraterrestre_aliado = models.BooleanField(
        verbose_name="Extraterrestre", help_text="")

    def __str__(self):
        return f'{self.nombre_aliado}'


class Companero_Equipo(models.Model):
    usuario = models.ForeignKey(
        Usuario, on_delete=models.CASCADE, verbose_name="Compañero de")
    nombre_companero = models.CharField(
        primary_key=True, max_length=30, verbose_name="Nombre", help_text="")
    telefono_companero = models.CharField(
        max_length=15, verbose_name="Teléfono", help_text="")
    email_companero = models.EmailField(
        verbose_name="E-mail", help_text="")
    cumpleanos_companero = models.DateField(
        blank=True, null=True, verbose_name="Cumpleaños", help_text="")

    def __str__(self):
        return f'{self.nombre_companero}'


class Enemigo(models.Model):
    usuario = models.ForeignKey(
        Usuario, on_delete=models.CASCADE, verbose_name="Enemigo de")
    alias_enemigo = models.CharField(
        primary_key=True, max_length=30, verbose_name="Alias del enemigo", help_text="")
    nombre_real_enemigo = models.CharField(
        max_length=30, verbose_name="Nombre real", help_text="")
    habilidad_principal_enemigo = models.CharField(
        max_length=20, verbose_name="Habilidad", help_text="")
    es_extraterrestre_enemigo = models.BooleanField(
        verbose_name="Es extraterrestre?", help_text="")

    def __str__(self):
        return f'{self.alias_enemigo}, {self.nombre_real_enemigo}'


class Persona_Salvada(models.Model):
    id_persona = models.PositiveIntegerField(
        primary_key=True, verbose_name="ID persona", help_text="")
    nombre_persona_salvada = models.CharField(
        max_length=30, verbose_name="Nombre", help_text="")
    edad_persona_salvada = models.PositiveIntegerField(
        verbose_name="Edad", help_text="")

    def __str__(self):
        return f'{self.nombre_persona_salvada}'


class Hecho(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(
        Usuario, on_delete=models.CASCADE, verbose_name="Salvador")
    persona = models.ForeignKey(
        Persona_Salvada, on_delete=models.CASCADE, verbose_name="Salvó a")
    lugar_hecho = models.CharField(
        max_length=20, verbose_name="Lugar", help_text="")
    fecha_hecho = models.DateField(
        verbose_name="Fecha", help_text="")
    descripcion_hecho = models.TextField(
        max_length=400, blank=True, null=True, verbose_name="Descripción", help_text="")

    class Meta:
        unique_together = ('persona', 'fecha_hecho', 'lugar_hecho',)

    def __str__(self):
        return f'{self.persona}'


class Mision(models.Model):
    usuario = models.ForeignKey(
        Usuario, on_delete=models.CASCADE, verbose_name="Misión para")
    codigo = models.CharField(
        primary_key=True, max_length=4, verbose_name="Código", help_text="")
    nombre_mision = models.CharField(
        max_length=20, unique=True, verbose_name="Nombre", help_text="")
    fecha = models.DateTimeField(
        unique=True, verbose_name="Fecha y hora", help_text="")
    opciones = [("PENDIENTE", "Pendiente"),
                ("CUMPLIDA", "Cumplida"), ("FALLIDA", "Fallida")]
    estado = models.CharField(
        choices=opciones, default="PENDIENTE", max_length=9, help_text="")
    observaciones = models.TextField(
        max_length=400, blank=True, null=True, help_text="")

    class Meta:
        unique_together = ('usuario', 'codigo',)
        unique_together = ('usuario', 'fecha')

    def __str__(self):
        return f'{self.codigo}, {self.nombre_mision}'


class Contrato(models.Model):
    usuario = models.ForeignKey(
        Usuario, on_delete=models.CASCADE, verbose_name="Contrato de", help_text="")
    ref_contrato = models.PositiveIntegerField(
        primary_key=True, verbose_name="Referencia", help_text="")
    nombre_patrocinador = models.CharField(
        max_length=30, verbose_name="Patrocinador")
    inicio_contrato = models.DateField(
        verbose_name="Inicio contrato", help_text="")
    fin_contrato = models.DateField(
        verbose_name="Fin contrato", help_text="")
    ganancia_por_contrato = models.FloatField(
        verbose_name="Ganancia por contrato", help_text="")

    def __str__(self):
        return f'{self.ref_contrato}, {self.nombre_patrocinador}'
