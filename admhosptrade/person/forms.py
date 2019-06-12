from django import forms
from django.forms import inlineformset_factory
from material import Layout, Fieldset, Span3, Row, Span12, Span9, Span4, Span2, Span8, Span5

from admhosptrade.person.models import Person


class PersonForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = (
            'name',
            'phone',
            'cpf_cnpj',
            'email',
            'nascimento',
            'rg',
            'cep',
            'logradouro',
            'numero',
            'bairro',
            'cidade',
            'estado',
        )
        exclude = ('priority',)

    layout = Layout(
        Fieldset("Pessoa",
                 Row(Span9('name'), Span3('nascimento'), ),
                 Row(Span4('phone'), Span4('cpf_cnpj'), Span4('rg')),
                 Row(Span12('email'), ),
                 ),
        Fieldset('Endereço',
                 Row(Span2('cep'), Span8('logradouro'), Span2('numero')),
                 Row(Span5('bairro'), Span5('cidade'), Span2('estado')))
        )