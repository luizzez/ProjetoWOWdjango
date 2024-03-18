from django.shortcuts import render, redirect, reverse
from .models import Carro, Usuario
from django.views.generic import TemplateView, ListView, DetailView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from .forms import CriarContaForm, FormHomePage
from django.http import HttpResponseRedirect


def logout_view(request):
    logout(request)
    return render(request, 'logout.html')


# def home_page(request):
#     return render(request, 'homepage.html')

# def home_page_carro(request):
#     context = {}
#     lista_carros = Carro.objects.all()
#     context['lista_carros'] = lista_carros
#     return render(request, 'homepageCarro.html', context)

class Homepage(FormView):
    template_name = 'homepage.html'
    form_class = FormHomePage

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('carro:homepageCarro')
        else:
            return super().get(request, *args, **kwargs)

    def get_success_url(self):
        email = self.request.POST.get('email')
        usuario = Usuario.objects.filter(email=email)
        if usuario:
            return reverse('carro:login')
        else:
            return reverse('carro:criarConta')


class HomepageCarro(LoginRequiredMixin, ListView):
    template_name = 'homepageCarro.html'
    model = Carro


class DetalhesCarro(LoginRequiredMixin, DetailView):
    template_name = 'detalhesCarro.html'
    model = Carro

    def get(self, request, *args, **kwargs):
        carro = self.get_object()
        carro.curtidas += 1
        carro.save()
        return super().get(request, *args, **kwargs)


class PesquisarCarro(LoginRequiredMixin, ListView):
    template_name = 'pesquisa.html'
    model = Carro

    def get_queryset(self):
        termo_pesquisa = self.request.GET.get('query')
        if termo_pesquisa:
            object_list = Carro.objects.filter(nome__contains=termo_pesquisa)
            return object_list
        else:
            return None


class PaginaPerfil(LoginRequiredMixin, UpdateView):
    template_name = 'editarperfil.html'
    model = Usuario
    fields = ['first_name', 'last_name', 'email']

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            if self.request.user.id != self.kwargs['pk']:
                return self.redirect_to_own_profile()
        else:
            return HttpResponseRedirect(reverse('carro:login'))
        return super().dispatch(request, *args, **kwargs)

    def redirect_to_own_profile(self):
        own_profile_url = reverse('carro:editarperfil', kwargs={'pk': self.request.user.id})
        return HttpResponseRedirect(own_profile_url)

    def get_success_url(self):
        return reverse('carro:homepageCarro:home_dhytpix')


class CriarConta(FormView):
    template_name = 'criarconta.html'
    form_class = CriarContaForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('carro:homepageCarro')

    # def get_context_data(self, **kwargs):
    #     context = super(DetalhesCarro, self).get_context_data(**kwargs)
    #     mais_acessados =
    #     context['mais_curtidos'] = mais_acessados
    #     return context
