import logging
from django.shortcuts import render

from guide.models import Card, CardType, Symbol, Wonder, WonderStep
from guide.logging import logging_setup

logging_setup()


def main_page(request):
    context = {
        'card_types': CardType.objects.order_by('type'),
        'wonders': Wonder.objects.order_by('name')
    }
    logging.debug(f'Main page context: {context}')
    return render(request, 'guide/main_page.html', context)


def symbols(request, card_type_id):
    context = {'symbols': Card.objects.filter(id=card_type_id)}
    logging.debug(f'Card type context: {context}')
    return render(request, 'guide/symbols.html', context)


def symbol_details(request, symbol_id):
    context = {'symbol': Symbol.objects.get(id=symbol_id)}
    logging.debug(f'Symbol details context: {context}')
    return render(request, 'guide/details.html', context)


def wonder_details(request, wonder_id):
    wonder = Wonder.objects.get(id=wonder_id)
    context = {
        'wonder': wonder,
        'steps': WonderStep.objects.filter(wonder=wonder)
    }
    logging.debug(f'Wonder details context: {context}')
    return render(request, 'guide/wonder.html', context)
