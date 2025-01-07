from django.db import models
from django.utils.timezone import now


class Localizacao(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nome


class Reuniao(models.Model):
    localizacao = models.ForeignKey(Localizacao, on_delete=models.CASCADE)
    data = models.DateField()
    horario = models.TimeField()
    descricao = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.localizacao} - {self.data} - {self.horario}"


class Contagem(models.Model):
    reuniao = models.ForeignKey(Reuniao, on_delete=models.CASCADE)
    host_nome = models.CharField(max_length=100)  # Campo para o nome do host
    total_pessoas = models.PositiveIntegerField(default=0)
    visitantes = models.PositiveIntegerField(default=0)
    criancas = models.PositiveIntegerField(default=0)
    conversoes = models.PositiveIntegerField(default=0)
    data_registro = models.DateTimeField(default=now)
    validado = models.BooleanField(default=False)

    def __str__(self):
        return f"Contagem de {self.host_nome} - {self.reuniao}"


class Validacao(models.Model):
    contagem = models.OneToOneField(Contagem, on_delete=models.CASCADE)
    observacoes = models.TextField(blank=True, null=True)
    fechado = models.BooleanField(default=False)

    def __str__(self):
        return f"Validação para {self.contagem}"
