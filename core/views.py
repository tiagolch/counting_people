from django.shortcuts import render, redirect
from .forms import ContagemForm
from django.shortcuts import render, get_object_or_404
from .models import Contagem
from django.utils.timezone import now
from django.db.models import Sum
from .models import Contagem, Localizacao, Reuniao


def enviar_contagem(request):
    if request.method == 'POST':
        form = ContagemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contagem_enviada')
    else:
        form = ContagemForm()

    return render(request, 'contagem_form.html', {'form': form})


def resumo_contagem(request):
    data_filtro = request.GET.get('data', now().date().strftime('%Y-%m-%d'))
    localizacao_id = request.GET.get('localizacao', '')
    horario_filtro = request.GET.get('horario', '')
    validado_filtro = request.GET.get('validado', '')

    localizacoes = Localizacao.objects.all()
    horarios = Reuniao.objects.filter(data=data_filtro).values_list('horario', flat=True).distinct()

    contagens = Contagem.objects.filter(reuniao__data=data_filtro)

    if localizacao_id:
        contagens = contagens.filter(reuniao__localizacao_id=localizacao_id)
        localizacao_selecionada = get_object_or_404(Localizacao, id=localizacao_id)
    else:
        localizacao_selecionada = None

    if horario_filtro:
        contagens = contagens.filter(reuniao__horario=horario_filtro)

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