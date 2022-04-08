from email.policy import default
from itertools import product
from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=100,help_text="Bu yerda kategoriya nomini kiriting.")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural="Kategoriyalar "
        verbose_name="Kategoriya "
class Products(models.Model):
    title=models.CharField(max_length=400,help_text="Bu yerda mahsulot nomini kiriting.")
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    cost=models.IntegerField(help_text="Bu yerda mahsulot narxini kiriting.")
    image=models.ImageField(upload_to='Products')
    desc=models.TextField(help_text="Bu yerda mahsulot haqida qisqacha ma'lumot kiriting.")
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural="Mahsulotlar "
        verbose_name="Mahsulot "
class Order(models.Model):
    
    token=models.CharField(max_length=400)
    def __str__(self):
        return f"{self.user} ning buyurtmalari"
    @property
    def all_summa(self):
        items=self.orderitem_set.all()
        total=sum([item.get_summa for item in items])
        return total
class OrderItem(models.Model):
    
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    def __str__(self):
        return self.order.user
    @property
    def get_summa(self):
        total=self.product.cost * self.quantity
        return total

class ShippingInfo(models.Model):
    name=models.CharField(max_length=400,null=True)
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    phone=models.CharField(max_length=400)
    adress=models.CharField(max_length=400)
    payment=models.BooleanField(default=False)

    def __str__(self):
        return self.order.user