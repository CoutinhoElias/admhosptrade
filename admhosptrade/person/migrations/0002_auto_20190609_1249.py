# Generated by Django 2.2.2 on 2019-06-09 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='complemento',
            field=models.CharField(default=1, max_length=100, verbose_name='Logradouro'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='inscricao_estadual',
            field=models.CharField(blank=True, max_length=18, null=True, verbose_name='Inscrição Estadual'),
        ),
        migrations.AddField(
            model_name='person',
            name='name_fantasy',
            field=models.CharField(default=1, max_length=100, verbose_name='Nome Fantasia'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='suframa',
            field=models.CharField(blank=True, max_length=18, null=True, verbose_name='SUFRAMA'),
        ),
    ]
