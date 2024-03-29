# Generated by Django 2.2.2 on 2019-06-16 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0003_person_related_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('created_on', models.DateField(auto_now_add=True, verbose_name='Criado em.')),
            ],
            options={
                'verbose_name': 'Categoria da Pessoa',
                'verbose_name_plural': 'Categoria de Pessoas',
                'ordering': ('created_on',),
            },
        ),
        migrations.AlterField(
            model_name='person',
            name='complemento',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Complemento'),
        ),
        migrations.AddField(
            model_name='person',
            name='category_person',
            field=models.ManyToManyField(related_name='category_person', to='person.PersonCategory'),
        ),
    ]
