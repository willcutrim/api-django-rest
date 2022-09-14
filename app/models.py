from django.db import models

class Produtos(models.Model):
    nome = models.CharField(max_length=155, blank=False, null=False)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    
