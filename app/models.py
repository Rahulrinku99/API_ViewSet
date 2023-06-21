from django.db import models

# Create your models here.
class ProductCategory(models.Model):
    PCname=models.CharField(max_length=100)
    PCid=models.IntegerField()

    def __str__(self) -> str:
        return self.PCname
    
class Product(models.Model):
    PCname=models.ForeignKey(ProductCategory,on_delete=models.CASCADE)
    Pid=models.IntegerField(primary_key=True)
    Pname=models.CharField(max_length=100)
    Price=models.IntegerField()

    def __str__(self) -> str:
        return self.Pname