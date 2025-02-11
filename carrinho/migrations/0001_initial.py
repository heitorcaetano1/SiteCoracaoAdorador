# Generated by Django 5.1.5 on 2025-02-08 01:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cliente', '0001_initial'),
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrinho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('ativa', models.BooleanField(default=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carrinho', to='cliente.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='ItemCarrinho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.PositiveIntegerField(default=1)),
                ('preco_unitario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('carrinho', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itens', to='carrinho.carrinho')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produtos.produto')),
            ],
        ),
    ]
