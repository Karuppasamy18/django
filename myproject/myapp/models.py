from django.db import models



class Basetable(models.Model):
    base_id = models.AutoField(primary_key=True)
    productname = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    
    

class Properties(models.Model):
    product_id = models.AutoField(primary_key=True)
    original_price = models.IntegerField()
    price = models.IntegerField()
    base_id= models.ForeignKey(Basetable, related_name="Properties", on_delete=models.CASCADE)

    
   
class Dimensions(models.Model):
    id = models.AutoField(primary_key=True)
    length = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
    base_id= models.ForeignKey(Basetable, on_delete=models.CASCADE,related_name='Dimensions')
    product_id = models.ForeignKey(Properties, on_delete=models.CASCADE)
   
class Images(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    is_listimage = models.BooleanField()
    url = models.CharField(max_length=100)   
    base_id= models.ForeignKey(Basetable, on_delete=models.CASCADE,related_name='Images')
    product_id = models.ForeignKey(Properties, on_delete=models.CASCADE)
    
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    productname = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    original_price = models.IntegerField()
    price = models.IntegerField()
    image_name = models.CharField(max_length=20)
    is_listimage = models.BooleanField(default=True)
    url = models.URLField(max_length=200)