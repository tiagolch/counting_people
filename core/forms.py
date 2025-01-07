from django import forms
from .models import Contagem

class ContagemForm(forms.ModelForm):
    host_nome = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite seu nome'
        })
    )

    class Meta:
        model = Contagem
        fields = ['reuniao', 'host_nome', 'total_pessoas', 'visitantes', 'criancas', 'conversoes']

    def __init__(self, *args, **kwargs):
        super(ContagemForm, self).__init__(*args, **kwargs)
        
        for field in self.fields:
            if field != 'host_nome':
                self.fields[field].widget.attrs.update({
                    'class': 'form-control mb-3',
                    'placeholder': f'Informe {self.fields[field].label.lower()}'
                })

        self.fields['total_pessoas'].widget.attrs.update({'min': 0})
        self.fields['visitantes'].widget.attrs.update({'min': 0})
        self.fields['criancas'].widget.attrs.update({'min': 0})
        self.fields['conversoes'].widget.attrs.update({'min': 0})
