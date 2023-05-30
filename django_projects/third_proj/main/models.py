from django.db import models

# Create your models here.

class Laptops(models.Model):
    title = models.CharField(max_length=150)
    color = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    img = models.ImageField(upload_to='images')
    desc = models.TextField(blank=True)
    tech_data = models.TextField(blank=True)
    
    class Meta:
        verbose_name = 'Laptop'
        verbose_name_plural = 'Laptops'

    def __str__(self) -> str:
        return f'{self.title}'