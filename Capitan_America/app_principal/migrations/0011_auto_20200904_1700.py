# Generated by Django 3.1 on 2020-09-04 22:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_principal', '0010_auto_20200901_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aliado',
            name='es_extraterrestre_aliado',
            field=models.BooleanField(help_text='Especifique si el aliado es extraterrestre o no', verbose_name='Extraterrestre'),
        ),
        migrations.AlterField(
            model_name='aliado',
            name='idioma_aliado',
            field=models.CharField(blank=True, help_text='Inserte el idioma nativo del aliado', max_length=20, null=True, verbose_name='Idioma'),
        ),
        migrations.AlterField(
            model_name='aliado',
            name='nombre_aliado',
            field=models.CharField(help_text='Inserte el nombre del aliado', max_length=30, primary_key=True, serialize=False, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='companero_equipo',
            name='cumpleanos_companero',
            field=models.DateField(blank=True, help_text='Inserte la fecha de cumpleaños del compañero de equipo', null=True, verbose_name='Cumpleaños'),
        ),
        migrations.AlterField(
            model_name='companero_equipo',
            name='email_companero',
            field=models.EmailField(help_text='Inserte el e-mail del compañero de equipo', max_length=254, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='companero_equipo',
            name='nombre_companero',
            field=models.CharField(help_text='Inserte el nombre del compañero de equipo', max_length=30, primary_key=True, serialize=False, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='companero_equipo',
            name='telefono_companero',
            field=models.CharField(help_text='Inserte el número de teléfono del compañero de equipo', max_length=15, verbose_name='Teléfono'),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='fin_contrato',
            field=models.DateField(help_text='Fecha de finalización del contrato', verbose_name='Fin contrato'),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='ganancia_por_contrato',
            field=models.FloatField(help_text='Monto ganado por contrato (MEDIDO EN PESOS COLOMBIANOS)', verbose_name='Ganancia por contrato'),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='inicio_contrato',
            field=models.DateField(help_text='Fecha de inicio del contrato', verbose_name='Inicio contrato'),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='ref_contrato',
            field=models.PositiveIntegerField(help_text='Código de referencia del contrato firmado', primary_key=True, serialize=False, verbose_name='Referencia'),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='usuario',
            field=models.ForeignKey(help_text='A quién le pertenece el contrato', on_delete=django.db.models.deletion.CASCADE, to='app_principal.usuario', verbose_name='Contrato de'),
        ),
        migrations.AlterField(
            model_name='enemigo',
            name='alias_enemigo',
            field=models.CharField(help_text='Inserte el alias del enemigo', max_length=30, primary_key=True, serialize=False, verbose_name='Alias'),
        ),
        migrations.AlterField(
            model_name='enemigo',
            name='es_extraterrestre_enemigo',
            field=models.BooleanField(help_text='Especifique si el enemigo es extraterrestre o no', verbose_name='Extraterrestre'),
        ),
        migrations.AlterField(
            model_name='enemigo',
            name='habilidad_principal_enemigo',
            field=models.CharField(help_text='Especifique la habilidad principal del enemigo', max_length=20, verbose_name='Habilidad ppal'),
        ),
        migrations.AlterField(
            model_name='enemigo',
            name='nombre_real_enemigo',
            field=models.CharField(help_text='Inserte el nombre real del enemigo', max_length=30, verbose_name='Nombre real'),
        ),
        migrations.AlterField(
            model_name='hecho',
            name='descripcion_hecho',
            field=models.TextField(blank=True, help_text='Inserte una breve descripción del acontecimiento', max_length=400, null=True, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='hecho',
            name='fecha_hecho',
            field=models.DateField(help_text='Inserte la fecha cuando la persona fue salvada', verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='hecho',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='hecho',
            name='lugar_hecho',
            field=models.CharField(help_text='Inserte el lugar donde la persona fue salvada', max_length=20, verbose_name='Lugar'),
        ),
        migrations.AlterField(
            model_name='mision',
            name='codigo',
            field=models.CharField(help_text='Inserte el código de la misión', max_length=4, primary_key=True, serialize=False, verbose_name='Código'),
        ),
        migrations.AlterField(
            model_name='mision',
            name='estado',
            field=models.CharField(choices=[('PENDIENTE', 'Pendiente'), ('CUMPLIDA', 'Cumplida'), ('FALLIDA', 'Fallida')], default='PENDIENTE', help_text='Especifique el estado de la misión', max_length=9),
        ),
        migrations.AlterField(
            model_name='mision',
            name='fecha',
            field=models.DateTimeField(help_text='Inserte la fecha y hora de la misión', unique=True, verbose_name='Fecha y hora'),
        ),
        migrations.AlterField(
            model_name='mision',
            name='nombre_mision',
            field=models.CharField(help_text='Inserte el nombre de la misión', max_length=20, unique=True, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='mision',
            name='observaciones',
            field=models.TextField(blank=True, help_text='Inserte una breve descripción de la misión', max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='persona_salvada',
            name='edad_persona_salvada',
            field=models.PositiveIntegerField(help_text='Inserte la edad de la persona salvada', verbose_name='Edad'),
        ),
        migrations.AlterField(
            model_name='persona_salvada',
            name='id_persona',
            field=models.PositiveIntegerField(help_text='Inserte el número de documento de identidad de la persona salvada', primary_key=True, serialize=False, verbose_name='ID persona'),
        ),
        migrations.AlterField(
            model_name='persona_salvada',
            name='nombre_persona_salvada',
            field=models.CharField(help_text='Inserte el nombre de la persona salvada', max_length=30, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='apellidos_usuario',
            field=models.CharField(help_text='Apellidos del usuario', max_length=30, verbose_name='Apellidos'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='dni_usuario',
            field=models.PositiveIntegerField(help_text='Número de documento de identificación', primary_key=True, serialize=False, verbose_name='DNI'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nombres_usuario',
            field=models.CharField(help_text='Nombres del usuario', max_length=30, verbose_name='Nombres'),
        ),
    ]
