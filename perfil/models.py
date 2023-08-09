from django.db import models

class Categoria(models.Model):
    categoria = models.CharField(max_length=50)
    essencial = models.BooleanField(default=False)
    valor_planejamento = models.FloatField(default=0)

    def __str__(self):
        return self.categoria

class Conta(models.Model):
    lista_banco = [
        ('NU', 'Nubank'),
        ('BD', 'Bradesco'),
        ('CE', 'Caixa Econômica'),
        ('SB', 'Sicoob'),
        ('SA', 'Santander')
    ]

    escolha_pessoa = [
        ('PF','Pessoa Física'),
        ('PJ','Pessoa Jurídica')
    ]
    apelido = models.CharField(max_length=40)
    banco = models.CharField(max_length=2, choices=lista_banco)
    tipo = models.CharField(max_length=2, choices=escolha_pessoa)
    valor = models.FloatField()
    icone = models.ImageField(upload_to='icones')

    def __str__(self):
        return self.apelido

