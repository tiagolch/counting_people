from django.db import models
from django.utils.timezone import now


class Localizacao(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = "Localização"
        verbose_name_plural = "Localizações"

    def __str__(self):
        return self.nome


class Reuniao(models.Model):
    localizacao = models.ForeignKey(Localizacao, on_delete=models.CASCADE)
    horario = models.TimeField()
    descricao = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = "Reunião"
        verbose_name_plural = "Reuniões"

    def __str__(self):
        return f"{self.localizacao} - {self.horario}"


class Contagem(models.Model):
    reuniao = models.ForeignKey(Reuniao, on_delete=models.CASCADE)
    data_reuniao = models.DateField(auto_now_add=True) 
    host_nome = models.CharField(max_length=100)  
    total_pessoas = models.PositiveIntegerField(default=0)
    visitantes = models.PositiveIntegerField(default=0)
    criancas = models.PositiveIntegerField(default=0)
    conversoes = models.PositiveIntegerField(default=0)
    data_registro = models.DateTimeField(default=now)
    validado = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Contagem"
        verbose_name_plural = "Contagens"

    def __str__(self):
        return f"Contagem de {self.host_nome} - {self.reuniao}"


class Validacao(models.Model):
    contagem = models.OneToOneField(Contagem, on_delete=models.CASCADE)
    observacoes = models.TextField(blank=True, null=True)
    fechado = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Validacao"
        verbose_name_plural = "Validacões"

    def __str__(self):
        return f"Validação para {self.contagem}"
