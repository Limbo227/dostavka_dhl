from django.db import models

# Create your models here.


class Dostavka(models.Model):
    amount = models.IntegerField('amount')
    length = models.IntegerField('length')
    width = models.IntegerField('width')
    height = models.IntegerField('height')
    scale = models.ForeignKey('Scale', verbose_name='scale', on_delete=models.CASCADE)
    weight = models.IntegerField('weight')
    scale_weight = models.ForeignKey('Scale_weight', verbose_name='Scale_weight', on_delete=models.CASCADE)
    total_price = models.IntegerField('total_price', default=0)

class Scale(models.Model):
    title = models.CharField('title', max_length=10)
    def __str__(self):
        return self.title


class Scale_weight(models.Model):
    title = models.CharField('title', max_length=10)

    def __str__(self):
        return self.title



