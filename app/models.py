from django.db import models

# Create your models here.
class Customer(models.Model):
    cus_name = models.CharField(max_length=100, null=False)
    cus_email = models.EmailField(unique=True, null=False)
    cus_mobile = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.cus_name
    

class Products(models.Model):
    cus = models.ManyToManyField("Customer")

    pro_name = models.CharField(max_length=100)
    pro_qty = models.PositiveIntegerField()

    def __str__(self):
        return self.pro_name
    