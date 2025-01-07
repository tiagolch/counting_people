from django.contrib import admin
from .models import Contagem, Reuniao, Localizacao, Validacao
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter

class ContagemAdmin(admin.ModelAdmin):
    list_display = ('reuniao__localizacao__nome','reuniao', 'host_nome', 'total_pessoas', 'visitantes', 'criancas', 'conversoes', 'validado', 'data_registro')
    list_editable = ("validado", "total_pessoas", "visitantes", "criancas", "conversoes",)
    list_filter = (
        'reuniao__localizacao__nome',
        'validado', 
        ('reuniao__data', DateRangeFilter),  
        'reuniao__localizacao', 
        'reuniao__horario',
        'host_nome',
    )
    search_fields = ('host_nome', 'reuniao__localizacao__nome')
    date_hierarchy = 'reuniao__data'

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.select_related('reuniao')
        return queryset

admin.site.register(Contagem, ContagemAdmin)
admin.site.register(Reuniao)
admin.site.register(Localizacao)
admin.site.register(Validacao)
