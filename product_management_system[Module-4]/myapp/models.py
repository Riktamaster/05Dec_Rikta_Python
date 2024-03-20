from django.db import models

# Create your models here.
class product_mst(models.Model):
    product_id=models.AutoField(primary_key=True)
    product_name=models.CharField(max_length=100)

    def __str__(self):
        return self.product_name

class product_sub_cat(models.Model):
    product=models.ForeignKey(product_mst, on_delete=models.CASCADE)
    product_price=models.DecimalField(max_digits=10, decimal_places=2)
    product_image=models.ImageField(upload_to='product_images/')
    product_model=models.CharField(max_length=100)
    product_ram=models.CharField(max_length=50)

    def __str__(self):
        return self.product.product_name