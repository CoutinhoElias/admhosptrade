# Generated by Django 2.2.2 on 2019-06-08 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('phone', models.CharField(blank=True, max_length=50, null=True, verbose_name='Telefone')),
                ('cpf_cnpj', models.CharField(blank=True, max_length=18, null=True, verbose_name='CPF/CNPJ')),
                ('rg', models.CharField(blank=True, max_length=18, null=True, verbose_name='RG')),
                ('nascimento', models.DateField(verbose_name='Data Nascimento')),
                ('email', models.CharField(max_length=50, null=True, verbose_name='E-Mail')),
                ('cep', models.CharField(max_length=10, null=True, verbose_name='Cep')),
                ('logradouro', models.CharField(max_length=100, verbose_name='Logradouro')),
                ('numero', models.CharField(max_length=10, verbose_name='Número')),
                ('bairro', models.CharField(max_length=50, verbose_name='Bairro')),
                ('cidade', models.CharField(max_length=50, verbose_name='Cidade')),
                ('estado', models.CharField(max_length=10, verbose_name='Estado')),
                ('priority', models.PositiveIntegerField(default=0, verbose_name='Prioridade')),
                ('created_on', models.DateField(auto_now_add=True, verbose_name='Criado em.')),
            ],
            options={
                'verbose_name': 'Pessoa',
                'verbose_name_plural': 'Pessoas',
                'ordering': ('created_on',),
            },
        ),
    ]