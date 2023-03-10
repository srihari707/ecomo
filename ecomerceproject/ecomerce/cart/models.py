from django.db import models
from ecomerceA.models import product


# Create your models here.
class cart(models.Model):
    Cart_id=models.CharField(max_length=250,blank=True)
    date_added=models.DateField(auto_now_add=True)

    class Meta:
        db_table='cart'
        ordering=['date_added']

    def __str__(self):
        return '{}'.format(self.Cart_id)

class cartitem(models.Model):
    Product=models.ForeignKey(product,on_delete=models.CASCADE)
    Cart=models.ForeignKey(cart,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    active=models.BooleanField(default=True)
    class Meta:
        db_table='cartitem'

    def __str__(self):
        return '{}'.format(self.Product)