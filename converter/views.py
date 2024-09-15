import requests
from django.shortcuts import render, redirect
from .forms import CurrencyConversionForm
from .models import ConversionHistory
from django.conf import settings
from decimal import Decimal

# Replace with your API key
API_KEY = '69c11fc5caa34e3796d3114f093435d7'
API_URL = 'https://openexchangerates.org/api/latest.json'



def get_available_currencies():
    # API call to fetch available currencies
    url = f"https://openexchangerates.org/api/currencies.json?app_id={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()  # Returns a dictionary of currency codes and names
    return {}


def convert_currency(amount, from_currency, to_currency):
    # Fetch live exchange rates
    url = f"{API_URL}?app_id={API_KEY}"
    response = requests.get(url)
    rates = response.json().get('rates')
    
    if from_currency not in rates or to_currency not in rates:
        return None, None

    # Convert the float rates to Decimal
    rate = Decimal(rates[to_currency]) / Decimal(rates[from_currency])

    
    # Convert the amount (Decimal) using the rate
    converted_amount = amount * rate

    converted_amount = round(converted_amount, 2)
    rate = round(rate, 2)

    return converted_amount, rate



def currency_converter_view(request):
    form = CurrencyConversionForm()
    conversion_result = None
    history = ConversionHistory.objects.all().order_by('-date')[:10]

    if request.method == 'POST':
        form = CurrencyConversionForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            from_currency = form.cleaned_data['from_currency'].upper()
            to_currency = form.cleaned_data['to_currency'].upper()

            converted_amount, rate = convert_currency(amount, from_currency, to_currency)

            if converted_amount is not None:
                # Save conversion to history
                ConversionHistory.objects.create(
                    from_currency=from_currency,
                    to_currency=to_currency,
                    amount=amount,
                    converted_amount=converted_amount,
                    conversion_rate=rate,
                )

                conversion_result = {
                    'amount': amount,
                    'from_currency': from_currency,
                    'to_currency': to_currency,
                    'converted_amount': converted_amount,
                    'rate': rate,
                }
            else:
                conversion_result = "Invalid currency."

    return render(request, 'converter/index.html', {
        'form': form,
        'conversion_result': conversion_result,
        'history': history,
    })

def clear_history(request):
    ConversionHistory.objects.all().delete()
    return redirect('converter')
