# Generated by Django 5.1 on 2024-09-08 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConversionHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_currency', models.CharField(max_length=10)),
                ('to_currency', models.CharField(max_length=10)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('converted_amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('conversion_rate', models.DecimalField(decimal_places=6, max_digits=12)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
