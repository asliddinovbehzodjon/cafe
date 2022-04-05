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
    user=models.CharField(max_length=400)
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    def __str__(self):
        return f"{self.user} ning buyurtmalari"