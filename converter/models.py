from django.db import models

class ConversionHistory(models.Model):
    from_currency = models.CharField(max_length=10)
    to_currency = models.CharField(max_length=10)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    converted_amount = models.DecimalField(max_digits=12, decimal_places=2)
    conversion_rate = models.DecimalField(max_digits=12, decimal_places=6)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.amount} {self.from_currency} to {self.to_currency}"
