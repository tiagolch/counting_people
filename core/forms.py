from django import forms
from django.utils.timezone import now
from .models import Contagem, Reuniao, Localizacao


class ContagemForm(forms.ModelForm):
    localizacao = forms.ModelChoiceField(
        queryset=Localizacao.objects.all(),
        empty_label="Selecione a Localização",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    horario = forms.ModelChoiceField(
        queryset=Reuniao.objects.none(),
        empty_label="Selecione o Horário",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    host_nome = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite seu nome'
        })
    )

    total_pessoas = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'min': 0
        }),
        initial=0
    )

    visitantes = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'min': 0
        }),
        initial=0
    )

    criancas = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'min': 0
        }),
        initial=0
    )

    conversoes = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'min': 0
        }),
        initial=0
    )

    voluntarios = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': '*Reservado para o líder',
            'aria-placeholder': '*Reservado para o líder',
            'label': 'Volutarios: Reservado para o líder',
            'min': 0, 
        }),
        initial=0
    )

    class Meta:
        model = Contagem
        fields = ['localizacao', 'horario', 'host_nome', 'total_pessoas', 'visitantes', 'criancas', 'conversoes', 'voluntarios']

    def __init__(self, *args, **kwargs):
        super(ContagemForm, self).__init__(*args, **kwargs)
        if 'localizacao' in self.data:
            try:
                localizacao_id = int(self.data.get('localizacao'))
                self.fields['horario'].queryset = Reuniao.objects.filter(localizacao_id=localizacao_id)
            except (ValueError, TypeError):
                self.fields['horario'].queryset = Reuniao.objects.none()

    def save(self, commit=True):
        contagem = super().save(commit=False)
        contagem.reuniao = self.cleaned_data['horario']  
        if commit:
            contagem.save()
        return contagem
