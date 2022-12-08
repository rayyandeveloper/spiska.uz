from django.contrib import admin
from django.db import models
from accounts.models import User

class Region(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name

class District(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name

class Shop(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Creator')
    admins = models.ManyToManyField(User, blank=True, related_name='Admins')
    members = models.ManyToManyField(User, blank=True, related_name='Members')

    image = models.ImageField(upload_to='shop-images/%Y/')
    name = models.CharField(max_length=200)
    bio = models.TextField(max_length=1000)

    currency = models.IntegerField(default=0)
    type = models.IntegerField(default=0)

    password = models.CharField(max_length=200)

    viloyat = models.ForeignKey(Region, on_delete=models.CASCADE)
    tuman = models.ForeignKey(District, on_delete=models.CASCADE)

    lat = models.CharField(max_length=200)
    lon = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    @admin.display(description='Creator\'s first name')
    def ret_hos_fir(self):
        return self.host.first_name

class Product(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)

    image1 = models.ImageField(upload_to='products-img/')
    image2 = models.ImageField(upload_to='products-img/', null=True, blank=True)
    image3 = models.ImageField(upload_to='products-img/', null=True, blank=True)

    name = models.CharField(max_length=200)
    description = models.TextField(max_length=2000)
    count = models.IntegerField()
    type = models.CharField(choices=(
            ('1', 'dona'),
            ('2', 'litr'),
            ('3', 'm2')
        ), max_length=200
    )
    currency = models.CharField(choices=(
            ('1', 'so\'m'),
            ('2', 'dollar'),
        ), max_length=200
    )

    entry_price = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    percent = models.IntegerField()
    selling_price = models.IntegerField()
    company = models.CharField(max_length=500)

    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    seens = models.ManyToManyField(User, related_name='seens', blank=True)
    

    barcode = models.CharField(max_length=100, default=00000000)

    def __str__(self) -> str:
        return self.name


class Promocode(models.Model):
    code = models.CharField(max_length=6)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, blank=True)
    percent = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.code} *** {self.shop.name}'


class Report(models.Model):
    product = models.ForeignKey(on_delete=models.CASCADE, to=Product)
    type = models.CharField(max_length=256)
    active = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.product.name


class Spiska(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)

    products = models.ManyToManyField(Product, blank=False, related_name='Products')
    lock_shop = models.BooleanField(default=False)    
    lock_user = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    all_products_price = models.IntegerField()
    money_type = models.CharField(choices=(
            ('1', 'so\'m'),
            ('2', 'dollar'),
        ), max_length=200
    )


class Category(models.Model):
    name = models.CharField(max_length=300)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.shop.name


