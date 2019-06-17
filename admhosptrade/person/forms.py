from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.forms import inlineformset_factory
from material import Layout, Fieldset, Span3, Row, Span12, Span9, Span4, Span2, Span8, Span5, Span6

from admhosptrade.person.models import Person, PersonContact


class PersonForm(forms.ModelForm):
    related_person = forms.ModelMultipleChoiceField(label='Pessoa Relacionada',
                                                    required=False,
                                                    queryset=Person.objects.all().order_by('name'),
                                                    )

    class Meta:
        model = Person
        fields = (
            'name',
            'name_fantasy',
            'phone',
            'cpf_cnpj',
            'email',
            'nascimento',
            'rg',
            'cep',
            'logradouro',
            'complemento',
            'numero',
            'bairro',
            'cidade',
            'estado',
            'category_person',
            'related_person',

        )
        exclude = ('priority', 'nascimento')

    layout = Layout(
        Fieldset("Pessoa",
                 Row(Span8('name'), Span4('name_fantasy'), ),
                 Row(Span4('phone'), Span4('cpf_cnpj'), Span4('rg')),
                 Row(Span12('email'), ),
                 ),

        Fieldset("Categorias da Pessoa",
                 Row(Span12('category_person'),)
                 ),

        Fieldset("Pessoa Relacionada",
                 Row(Span12('related_person'), )
                 ),

        Fieldset('Endereço',
                 Row(Span2('cep'), Span6('logradouro'), Span2('complemento'), Span2('numero')),
                 Row(Span5('bairro'), Span5('cidade'), Span2('estado')))
        )


# class SearchForm(forms.ModelForm):
#
#     class Meta:
#         model = Search
#         fields = '__all__'
#         exclude = ()
#
#     layout = Layout(
#         Fieldset("Responda com Calma.", Row('person', 'search_key'), Row('researched',),))
#
#
PersonContactFormSet = inlineformset_factory(Person, PersonContact,
                                             # widgets={'name': forms.TextInput(attrs={'width': '110%'}), },
                                             exclude=('id',),
                                             can_delete=True,
                                             fields=('kind',
                                                     'kind_text',
                                                     'kind_text',
                                                     'whatsapp',
                                                     'name',
                                                     'last_name',
                                                     'alias'),
                                             extra=5)
