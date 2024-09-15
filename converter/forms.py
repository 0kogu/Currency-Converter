from django import forms

# List of currency choices (abbreviations)
CURRENCY_CHOICES = [
    ('USD', 'USD'),
    ('EUR', 'EUR'),
    ('GBP', 'GBP'),
    ('JPY', 'JPY'),
    ('AUD', 'AUD'),
    ('CAD', 'CAD'),
    ('CNY', 'CNY'),
    # Add more currencies as needed or dynamically load them
]

class CurrencyConversionForm(forms.Form):
    amount = forms.DecimalField(max_digits=12, decimal_places=2, label="Amount")
    from_currency = forms.ChoiceField(choices=CURRENCY_CHOICES, label="From Currency")
    to_currency = forms.ChoiceField(choices=CURRENCY_CHOICES, label="To Currency")
