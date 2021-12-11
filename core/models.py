from django.db import models
from stdimage.models import StdImageField

ICONE_CHOICES = (
    ('lni-cog', 'Engrenagem'),
    ('lni-stats-up', 'Gráfico'),
    ('lni-users', 'Usuários'),
    ('lni-layers', 'Design'),
    ('lni-mobile', 'Mobile'),
    ('lni-rocket', 'Foguete'),
    ('lni-users', 'Usuários'),
    ('lni-asterisk', 'Asterisco'),
    ('lni-tag', 'Tag'),
    ('lni-envelope', 'Envelope'),
    ('lni-world', 'World'),
)


class Base(models.Model):
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)
    active = models.BooleanField('Ativo', default=True)

    class Meta:
        abstract = True


class service(Base):
    service = models.CharField(verbose_name='Serviço', max_length=100)
    description = models.TextField(verbose_name='Descrição', max_length=200)
    icone = models.CharField('Ícone', max_length=20, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.service


class Position(Base):
    position = models.CharField(verbose_name='Nome', max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.position


class Employee(Base):
    name = models.CharField(verbose_name='Nome', max_length=100)
    position = models.ForeignKey(Position, verbose_name='Cargo', on_delete=models.CASCADE)
    bio = models.TextField(verbose_name='Bio', max_length=200)
    imagem = StdImageField(verbose_name='Imagem', upload_to='team', variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
    facebook = models.CharField(verbose_name='Facebook', max_length=100, default='#')
    twitter = models.CharField(verbose_name='Twitter', max_length=100, default='#')
    instagram = models.CharField(verbose_name='Instagram', max_length=100, default='#')

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

    def __str__(self):
        return self.name