from . import views
from django.urls import path

urlpatterns = [
    # example: /guide
    path('', views.main_page, name='main_page'),
    # example: /cards/1
    path('cards/<int:card_type_id>', views.symbols, name='symbols'),
    # example: /details/19
    path('details/<int:symbol_id>', views.symbol_details, name='symbol_details'),
    # example: /wonder/3
    path('wonder/<int:wonder_id>', views.wonder_details, name='wonder_details'),
]
