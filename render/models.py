from django.db import models

class Task(models.Model):
    titulo = models.CharField(max_length=128)
    completado = models.BooleanField(default=False)
    criado_em = models.DateTimeField(auto_now_add=True,blank=True,null=True)

    class Meta:
        verbose_name = ("task")
        verbose_name_plural = ("tasks")

    def __str__(self):
        return self.titulo
