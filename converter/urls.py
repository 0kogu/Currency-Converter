from django.urls import path
from .views import currency_converter_view, clear_history

urlpatterns = [
    path('', currency_converter_view, name='converter'),
    path('clear-history/', clear_history, name='clear_history'),
]
