from django.shortcuts import render, redirect
from .forms import ContagemForm
from django.shortcuts import render, get_object_or_404
from .models import Contagem
from django.utils.timezone import now
from django.db.models import Sum
from .models import Contagem, Localizacao, Reuniao
from django.http import JsonResponse
from datetime import datetime
from django.contrib import messages


def enviar_contagem(request):
    if request.method == 'POST':
        form = ContagemForm(request.POST)
        if form.is_valid():
            if form.cleaned_data.get('horario'):
                form.save()
                messages.success(request, 'Contagem enviada com sucesso!')
                return redirect('enviar_contagem')
            else:
                messages.error(request, 'Por favor, selecione um horário válido.')
        else:
            messages.error(request, 'Corrija os erros no formulário.')
    else:
        form = ContagemForm()
    
    return render(request, 'contagem_form.html', {'form': form})

def get_horarios(request):
    localizacao_id = request.GET.get('localizacao')
    horarios = Reuniao.objects.filter(localizacao_id=localizacao_id).values('id', 'horario')

    return JsonResponse({'horarios': list(horarios)})


def resumo_contagem(request):
    data_filtro = request.GET.get('data', now().date().strftime('%Y-%m-%d'))

    data_filtro_iso = data_filtro

    localizacao_id = request.GET.get('localizacao', '')
    horario_filtro = request.GET.get('horario', '')
    validado_filtro = request.GET.get('validado', '')

    localizacoes = Localizacao.objects.all()
    horarios = Reuniao.objects.values_list('horario', flat=True).distinct()

    contagens = Contagem.objects.filter(data_reuniao=data_filtro_iso)

    if localizacao_id:
        contagens = contagens.filter(reuniao__localizacao_id=localizacao_id)
        localizacao_selecionada = get_object_or_404(Localizacao, id=localizacao_id)
    else:
        localizacao_selecionada = None

    if horario_filtro:
        try:
            horario_formatado = datetime.strptime(horario_filtro, '%H:%M').time()
            contagens = contagens.filter(reuniao__horario=horario_formatado)
        except ValueError:
            pass  # Evita erro se o horário não estiver no formato correto

    if validado_filtro == '1':
        contagens = contagens.filter(validado=True)
    elif validado_filtro == '0':
        contagens = contagens.filter(validado=False)

    totais = contagens.aggregate(
        total_pessoas=Sum('total_pessoas'),
        total_visitantes=Sum('visitantes'),
        total_criancas=Sum('criancas'),
        total_conversoes=Sum('conversoes')
    )

    return render(request, 'resumo_contagem.html', {
        'contagens': contagens,
        'localizacoes': localizacoes,
        'horarios': horarios,
        'data_filtro': data_filtro,
        'localizacao_filtro': localizacao_id,
        'localizacao_selecionada': localizacao_selecionada,
        'horario_filtro': horario_filtro,
        'validado_filtro': validado_filtro,
        'totais': totais
    })


def contagem_enviada(request):
    return render(request, 'contagem_enviada.html')

def atualizar_validacao(request, contagem_id):
    if request.method == 'POST':
        contagem = Contagem.objects.get(id=contagem_id)
        contagem.validado = not contagem.validado  # Alterna entre True e False
        contagem.save()
        return JsonResponse({'status': 'success', 'validado': contagem.validado})
    return JsonResponse({'status': 'error'}, status=400)
