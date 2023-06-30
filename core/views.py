from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ControleVisitanteForm, ControleChaveForm, SetorChaveForm, ControleVeiculoForm, SetorVeiculoForm
from .models import ControleVisitante, ControleVeiculo, ControleChave, SetorChave, SetorVeiculo


# Create your views here.
@login_required()
def visitante(request):
    template_core = 'core/visitante/lista_visitante.html'
    visitantes = ControleVisitante.objects.all()
    if request.method == "POST":
        form = ControleVisitanteForm(request.POST)
        if form.is_valid():
            registro = form.save(commit=False)
            registro.porteiro = request.user
            registro.save() 
            return redirect('visitante')
        else:
            print(form.errors)
    else:
        form = ControleVisitanteForm()
    
    context = {
        'form': form,
        'visitantes': visitantes
    }
    return render(request, template_core, context)

@login_required()
def finalizarSaida(request):
    if request.method == "POST":
        id = request.POST.get('id')
        print(id)
        registroVisitante = ControleVisitante.objects.get(id=id)
        registroVisitante.registro_saida = timezone.now()
        registroVisitante.save()
        return redirect('visitante')
    
@login_required()   
def controleChave(request):
    template_name = 'core/controle_chave/lista_controleChave.html'
    chaves = ControleChave.objects.all()
    if request.method == 'POST':
        form = ControleChaveForm(request.POST)
        form_setor = SetorChaveForm(request.POST)    
        if 'formControleChave' in request.POST:
            print("Controle chave")
            form = ControleChaveForm(request.POST)
            registro = form.save(commit=False)
            registro.porteiro = request.user
            registro.save()
            return redirect('controle_chave')
        if 'formSetor' in request.POST:
            print("Controle Setor")
            form_setor = SetorChaveForm(request.POST)
            form_setor.save()
            return redirect('controle_chave')
    else:
        form = ControleChaveForm()
        form_setor = SetorChaveForm()
    
    context = {
        'form': form,
        'chaves': chaves,
        'form_setor': form_setor
    }
    return render(request, template_name, context)

@login_required()
def finalizarEntregaChave(request):
    if request.method == "POST":
        id = request.POST.get('id')
        print(id)
        print(timezone.now())
        registroChave = ControleChave.objects.get(id=id)
        registroChave.registro_recebimento = timezone.now()
        registroChave.save()
        return redirect('controle_chave')

@login_required()
def controleVeiculo(request):
    template_name = 'core/veiculo/lista_controleVeiculo.html'
    veiculos = ControleVeiculo.objects.all().order_by("-registro_entrada")
    if request.method == 'POST':
        form = ControleVeiculoForm(request.POST)
        form_setor = SetorVeiculoForm(request.POST)    
        if 'formControleVeiculo' in request.POST:
            print("Controle de veiculo")
            form = ControleVeiculoForm(request.POST)
            if form.is_valid():
                registro = form.save(commit=False)
                registro.porteiro = request.user
                registro.save()
                return redirect('controle_veiculo')
            else:
                print(form.errors)
        if 'formSetorVeiculo' in request.POST:
            print("Controle Setor")
            form_setor = SetorVeiculoForm(request.POST)
            form_setor.save()
            return redirect('controle_veiculo')
    else:
        form = ControleVeiculoForm()
        form_setor = SetorVeiculoForm()
    
    context = {
        'form': form,
        'veiculos': veiculos,
        'form_setor': form_setor
    }
    return render(request, template_name, context)

@login_required()
def finalizarSaidaVeiculo(request):
    if request.method == "POST":
        id = request.POST.get('id')
        print(id)
        registroVeiculo = ControleVeiculo.objects.get(id=id)
        registroVeiculo.registro_saida = timezone.now()
        registroVeiculo.save()
        return redirect('controle_veiculo')
