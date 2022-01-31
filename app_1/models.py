from django.db import models

# Create your models here.


class Todo(models.Model):
    type = (
        ('active', 'active'),
        ('soon', 'soon'),
        ('done', 'done')
    )
    sarlavha = models.CharField(max_length=50)
    sana = models.DateField()
    batafsil = models.TextField(max_length=100)
    status = models.CharField(max_length=10, choices=type)

