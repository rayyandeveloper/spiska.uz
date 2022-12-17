from django.db import models

class ProductLog(models.Model):
    price = models.IntegerField()
    main_price = models.IntegerField()
    count = models.IntegerField()
    name = models.CASCADE


class Log(models.Model):
    data = models.DateTimeField(auto_now_add=True)

