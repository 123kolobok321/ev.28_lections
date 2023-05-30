from django.db import models

# Create your models here.
class Phones(models.Model):
    title = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    image = models.ImageField(upload_to='imeges')
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Phone'
        verbose_name_plural = 'Phones'

    def __str__(self) -> str:
        return f'{self.title}'