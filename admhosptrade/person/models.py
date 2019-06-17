from django.db import models

# Create your models here.
KIND_CONTACT = (
    ('0', 'Telefone Fixo'),
    ('1', 'Celular 1'),
    ('2', 'E-Mail'),
)


class Person(models.Model):
    name = models.CharField('Nome', max_length=100)
    name_fantasy = models.CharField('Nome Fantasia', max_length=100)
    phone = models.CharField('Telefone', max_length=50, null=True, blank=True)
    cpf_cnpj = models.CharField('CPF/CNPJ', max_length=18, null=True, blank=True)
    inscricao_estadual = models.CharField('Inscrição Estadual', max_length=18, null=True, blank=True)
    suframa = models.CharField('SUFRAMA', max_length=18, null=True, blank=True)
    rg = models.CharField('RG', max_length=18, null=True, blank=True)
    nascimento = models.DateField('Data Nascimento', null=True, blank=False)
    email = models.CharField('E-Mail', max_length=50, null=True, blank=False)
    cep = models.CharField('Cep', max_length=10, null=True, blank=False)
    logradouro = models.CharField('Logradouro', max_length=100)
    complemento = models.CharField('Complemento', max_length=100, null=True, blank=True)
    numero = models.CharField('Número', max_length=10, null=False, blank=False)
    bairro = models.CharField('Bairro', max_length=50, null=False, blank=False)
    cidade = models.CharField('Cidade', max_length=50, null=False, blank=False)
    estado = models.CharField('Estado', max_length=10, null=False, blank=False)
    related_person = models.ManyToManyField('self', related_name='related_person')
    category_person = models.ManyToManyField('person.personcategory', related_name='category_person')

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
        self.complemento = self.complemento.upper()

        super(Person, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class PersonContact(models.Model):
    person = models.ForeignKey('person.person', related_name='Pessoa', on_delete=models.CASCADE)
    kind = models.TextField('Tipo Contato', max_length=1, choices=KIND_CONTACT)
    kind_text = models.CharField('Conteúdo Tipo', max_length=15)
    whatsapp = models.BooleanField('Whatsapp')
    name = models.CharField('Nome', max_length=100)
    last_name = models.CharField('Sobrenome', max_length=100)
    alias = models.CharField('Apelido', max_length=100)
    created_on = models.DateField(
        'Criado em.',
        auto_now_add=True,
        auto_now=False
    )

    class Meta:
        ordering = ('created_on',)
        verbose_name = 'Contato da Pessoa'
        verbose_name_plural = 'Contatos de Pessoas'

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        self.kind_text = self.kind_text.lower()
        self.last_name = self.last_name.upper()
        self.alias = self.alias.upper()

        super(PersonContact, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class PersonCategory(models.Model):
    name = models.CharField('Nome', max_length=100)
    created_on = models.DateField(
        'Criado em.',
        auto_now_add=True,
        auto_now=False
    )

    class Meta:
        ordering = ('created_on',)
        verbose_name = 'Categoria da Pessoa'
        verbose_name_plural = 'Categoria de Pessoas'

    def save(self, *args, **kwargs):
        self.name = self.name.upper()

        super(PersonCategory, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
