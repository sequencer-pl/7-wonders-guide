from django.contrib import admin

from guide.models import Card, CardType, Expansion, Symbol, Wonder, WonderStep

admin.site.register(Expansion)
admin.site.register(Symbol)
admin.site.register(CardType)
admin.site.register(Card)
admin.site.register(Wonder)
admin.site.register(WonderStep)
