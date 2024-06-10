from django.db import models
from shop.models import Product
from coupons.models import Coupon
from django.core.validators import MaxValueValidator,MinValueValidator
from decimal import Decimal
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Order(models.Model):
    first_name=models.CharField(_('fisrt name'),max_length=50)
    last_name=models.CharField(_('last name'),max_length=50)
    email=models.EmailField(_('e-mail'))
    address=models.CharField(_('address'),max_length=200)
    postal_code=models.CharField(_('postal code'),max_length=20)
    city=models.CharField(_('city'),max_length=100)
    created=models.DateTimeField(_('created'),auto_now_add=True)
    updated=models.DateTimeField(_('updated'),auto_now=True)
    paid=models.BooleanField(_('paid'),default=False)

    coupon=models.ForeignKey(Coupon,on_delete=models.SET_NULL,related_name='orders',null=True,blank=True)
    discount=models.IntegerField(default=0,validators=[MaxValueValidator(100),MinValueValidator(0)])


    class Meta:
        ordering=['-created']
        indexes=[
        models.Index(fields=['-created']),
        ]
    def __str__(self):
        return f'Order {self.id}'

    def get_total_cost(self):
        total_cost=self.get_total_cost_before_discount()

        return total_cost - self.get_discount()

    def get_total_cost_before_discount(self):
        return sum(item.get_cost() for item in self.items.all())

    def get_discount(self):
        total_cost=self.get_total_cost_before_discount()
        if self.discount:
            return total_cost * (self.discount / Decimal(100))
        return Decimal(0)


class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='items')
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='order_items')
    price=models.DecimalField(max_digits=10,decimal_places=2)
    quantity=models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity