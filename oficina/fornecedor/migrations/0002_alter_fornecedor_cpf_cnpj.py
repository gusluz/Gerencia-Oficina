# Generated by Django 4.2.15 on 2024-10-16 03:28

import cliente.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fornecedor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fornecedor',
            name='cpf_cnpj',
            field=models.CharField(max_length=18, validators=[cliente.validators.validate_cpf_cnpj], verbose_name='CPF/CNPJ'),
        ),
    ]
