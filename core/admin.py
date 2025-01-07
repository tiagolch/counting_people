from django.contrib import admin
from .models import Localizacao, Reuniao,  Contagem, Validacao

admin.site.register(Localizacao)
admin.site.register(Reuniao)
admin.site.register(Contagem)
admin.site.register(Validacao)
