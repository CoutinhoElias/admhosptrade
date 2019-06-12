from django.db import models

# Create your models here.
# KIND_CONTACT = (
#     ('0', 'Telefone Fixo'),
#     ('1', 'Celular 1'),
#     ('2', 'Celular 2'),
#     ('3', 'Celular 3'),
#     ('4', 'E-Mail'),
#     ('5', 'Telefone Trabalho'),
# )
#


class Person(models.Model):
    name = models.CharField('Nome', max_length=100)
    name_fantasy = models.CharField('Nome Fantasia', max_length=100)
    phone = models.CharField('Telefone', max_length=50, null=True, blank=True)
    cpf_cnpj = models.CharField('CPF/CNPJ', max_length=18, null=True, blank=True)
    inscricao_estadual = models.CharField('Inscrição Estadual', max_length=18, null=True, blank=True)
    suframa = models.CharField('SUFRAMA', max_length=18, null=True, blank=True)
    rg = models.CharField('RG', max_length=18, null=True, blank=True)
    nascimento = models.DateField('Data Nascimento')
    email = models.CharField('E-Mail', max_length=50, null=True, blank=False)
    cep = models.CharField('Cep', max_length=10, null=True, blank=False)
    logradouro = models.CharField('Logradouro', max_length=100)
    complemento = models.CharField('Logradouro', max_length=100)
    numero = models.CharField('Número', max_length=10, null=False, blank=False)
    bairro = models.CharField('Bairro', max_length=50, null=False, blank=False)
    cidade = models.CharField('Cidade', max_length=50, null=False, blank=False)
    estado = models.CharField('Estado', max_length=10, null=False, blank=False)
    # related_person = models.ForeignKey("self", null=True,
    #                                    blank=True,
    #                                    related_name="children",
    #                                    on_delete=models.CASCADE,
    #                                    verbose_name="Pessoa Relacionada")
    
    priority = models.PositiveIntegerField('Prioridade', default=0)
    created_on = models.DateField(
        'Criado em.',
        auto_now_add=True,
        auto_now=False
    )

    class Meta:
        ordering = ('created_on',)
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        self.email = self.email.lower()
        self.logradouro = self.logradouro.upper()
        self.bairro = self.bairro.upper()
        self.cidade = self.cidade.upper()
        self.estado = self.estado.upper()

        super(Person, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

