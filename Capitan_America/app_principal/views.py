from app_principal.models import Usuario, Contrato, Aliado, Companero_Equipo, Persona_Salvada, Hecho, Enemigo, Mision
from app_principal.forms import AgregarUsuariosForm, AgregarAliadosForm, AgregarCompanerosForm, AgregarEnemigosForm, AgregarHechosForm, AgregarSalvadosForm, AgregarMisionesForm, AgregarContratosForm
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.


class Home(TemplateView):
    template_name = 'app_principal/home.html'


# AGREGAR

class CrearUsuarios(CreateView):
    model = Usuario
    template_name = 'app_principal/crearUsuarios.html'
    context_object_name = 'usuario_form'
    form_class = AgregarUsuariosForm
    success_url = reverse_lazy('ListarUsuarios')


class CrearAliados(CreateView):
    model = Aliado
    template_name = 'app_principal/crearAliados.html'
    context_object_name = 'aliado_form'
    form_class = AgregarAliadosForm
    success_url = reverse_lazy('ListarAliados')


class CrearCompaneros(CreateView):
    model = Companero_Equipo
    template_name = 'app_principal/crearCompaneros.html'
    context_object_name = 'companero_form'
    form_class = AgregarCompanerosForm
    success_url = reverse_lazy('ListarCompaneros')


class CrearEnemigos(CreateView):
    model = Enemigo
    template_name = 'app_principal/crearEnemigos.html'
    context_object_name = 'enemigo_form'
    form_class = AgregarEnemigosForm
    success_url = reverse_lazy('ListarEnemigos')


class CrearHechos(CreateView):
    model = Hecho
    template_name = 'app_principal/crearHechos.html'
    context_object_name = 'hecho_form'
    form_class = AgregarHechosForm
    success_url = reverse_lazy('ListarHechos')


class CrearSalvados(CreateView):
    model = Persona_Salvada
    template_name = 'app_principal/crearSalvados.html'
    context_object_name = 'salvado_form'
    form_class = AgregarSalvadosForm
    success_url = reverse_lazy('ListarPersonas')


class CrearMisiones(CreateView):
    model = Mision
    template_name = 'app_principal/crearMisiones.html'
    context_object_name = 'mision_form'
    form_class = AgregarMisionesForm
    success_url = reverse_lazy('ListarMisiones')


class CrearContratos(CreateView):
    model = Contrato
    template_name = 'app_principal/crearContratos.html'
    context_object_name = 'contrato_form'
    form_class = AgregarContratosForm
    success_url = reverse_lazy('ListarContratos')


# LISTAR

class ListarUsuarios(ListView):
    model = Usuario
    template_name = 'app_principal/listarUsuarios.html'
    context_object_name = 'usuarios'


class ListarAliados(ListView):
    model = Aliado
    template_name = 'app_principal/listarAliados.html'
    context_object_name = 'aliados'


class ListarCompaneros(ListView):
    model = Companero_Equipo
    template_name = 'app_principal/listarCompaneros.html'
    context_object_name = 'companeros'


class ListarEnemigos(ListView):
    model = Enemigo
    template_name = 'app_principal/listarEnemigos.html'
    context_object_name = 'enemigos'


class ListarHechos(ListView):
    model = Hecho
    template_name = 'app_principal/listarHechos.html'
    context_object_name = 'hechos'


class ListarPersonas(ListView):
    model = Persona_Salvada
    template_name = 'app_principal/listarPersonas.html'
    context_object_name = 'personas'


class ListarMisiones(ListView):
    model = Mision
    template_name = 'app_principal/listarMisiones.html'
    context_object_name = 'misiones'


class ListarContratos(ListView):
    model = Contrato
    template_name = 'app_principal/listarContratos.html'
    context_object_name = 'contratos'


# EDITAR

class EditarUsuarios(UpdateView):
    model = Usuario
    template_name = 'app_principal/crearUsuarios.html'
    context_object_name = 'usuario'
    form_class = AgregarUsuariosForm
    success_url = reverse_lazy('ListarUsuarios')


class EditarAliados(UpdateView):
    model = Aliado
    template_name = 'app_principal/crearAliados.html'
    context_object_name = 'aliado'
    form_class = AgregarAliadosForm
    success_url = reverse_lazy('ListarAliados')


class EditarCompaneros(UpdateView):
    model = Companero_Equipo
    template_name = 'app_principal/crearCompaneros.html'
    context_object_name = 'companero'
    form_class = AgregarCompanerosForm
    success_url = reverse_lazy('ListarCompaneros')


class EditarEnemigos(UpdateView):
    model = Enemigo
    template_name = 'app_principal/crearEnemigos.html'
    context_object_name = 'enemigo'
    form_class = AgregarEnemigosForm
    success_url = reverse_lazy('ListarEnemigos')


class EditarHechos(UpdateView):
    model = Hecho
    template_name = 'app_principal/crearHechos.html'
    context_object_name = 'hecho'
    form_class = AgregarHechosForm
    success_url = reverse_lazy('ListarHechos')


class EditarPersonas(UpdateView):
    model = Persona_Salvada
    template_name = 'app_principal/crearSalvados.html'
    context_object_name = 'salvado'
    form_class = AgregarSalvadosForm
    success_url = reverse_lazy('ListarPersonas')


class EditarMisiones(UpdateView):
    model = Mision
    template_name = 'app_principal/crearMisiones.html'
    context_object_name = 'mision'
    form_class = AgregarMisionesForm
    success_url = reverse_lazy('ListarMisiones')


class EditarContratos(UpdateView):
    model = Contrato
    template_name = 'app_principal/crearContratos.html'
    context_object_name = 'contrato'
    form_class = AgregarContratosForm
    success_url = reverse_lazy('ListarContratos')


# ELIMINAR

class EliminarUsuarios(DeleteView):
    model = Usuario
    template_name = 'app_principal/eliminarUsuarios.html'
    context_object_name = 'usuario'
    form_class = AgregarUsuariosForm
    success_url = reverse_lazy('ListarUsuarios')


class EliminarAliados(DeleteView):
    model = Aliado
    template_name = 'app_principal/eliminarAliados.html'
    context_object_name = 'aliado'
    form_class = AgregarAliadosForm
    success_url = reverse_lazy('ListarAliados')


class EliminarCompaneros(DeleteView):
    model = Companero_Equipo
    template_name = 'app_principal/eliminarCompaneros.html'
    context_object_name = 'companero'
    form_class = AgregarCompanerosForm
    success_url = reverse_lazy('ListarCompaneros')


class EliminarEnemigos(DeleteView):
    model = Enemigo
    template_name = 'app_principal/eliminarEnemigos.html'
    context_object_name = 'enemigo'
    form_class = AgregarEnemigosForm
    success_url = reverse_lazy('ListarEnemigos')


class EliminarPersonas(DeleteView):
    model = Persona_Salvada
    template_name = 'app_principal/eliminarPersonas.html'
    context_object_name = 'salvado'
    form_class = AgregarSalvadosForm
    success_url = reverse_lazy('ListarPersonas')


class EliminarMisiones(DeleteView):
    model = Mision
    template_name = 'app_principal/eliminarMisiones.html'
    context_object_name = 'mision'
    form_class = AgregarMisionesForm
    success_url = reverse_lazy('ListarMisiones')


class EliminarContratos(DeleteView):
    model = Contrato
    template_name = 'app_principal/eliminarContratos.html'
    context_object_name = 'contrato'
    form_class = AgregarContratosForm
    success_url = reverse_lazy('ListarContratos')


class EliminarHechos(DeleteView):
    model = Hecho
    template_name = 'app_principal/eliminarHechos.html'
    context_object_name = 'hecho'
    form_class = AgregarHechosForm
    success_url = reverse_lazy('ListarHechos')
