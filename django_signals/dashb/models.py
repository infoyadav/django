from django.db import models
from users.models import UserProfile
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

from django.utils.html import mark_safe

from django.utils import timezone

# Create your models here.
class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    cname = models.CharField(verbose_name = "Add Category Here", max_length=150, null=True)
    at_updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.cname


class Product(models.Model):
    # category_type = (
    #     ('Clothes', 'Clothes'),
    #     ('Shoes', 'Shoes'),
    #     ('Electronic', 'Electronic'),
    #     ('Vegitable', 'Vegitable'),
    #     ('Foods', 'Foods'),
    # )
    p_id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, verbose_name="Choose Category Here", on_delete=models.CASCADE)
    pname = models.CharField(verbose_name="Product Name", max_length=150)
    ptitle = models.CharField(verbose_name="Product Title", max_length=150, null=True)
    quantity = models.PositiveIntegerField(verbose_name="Product Quantity")
    image = models.ImageField(upload_to='%Y-%m-%d/', validators=[FileExtensionValidator(allowed_extensions=['jpeg', 'jpg', 'png'])], default='avtar.png')
    price = models.PositiveIntegerField(null=True)

    # from PIL import Image

    # # resizing images
    # def save(self, *args, **kwargs):
    #     super().save()

    #     img = Image.open(self.avatar.path)

    #     if image.height > 100 or image.width > 100:
    #         new_img = (100, 100)
    #         image.thumbnail(new_img)
    #         image.save(self.avatar.path)

    def __str__(self):
        return self.pname
    
    # def image_tag(self):
    #         return mark_safe('<img src="/directory/%s" width="150" height="150" />' % (self.image))
    # image_tag.short_description = 'Image'

class Order(models.Model):
    user = models.ForeignKey(User, verbose_name="User Name", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name="Product Name", on_delete=models.CASCADE)
    order_quantity = models.PositiveIntegerField(verbose_name="Order Quantity")
    # date_of_oder = models.DateTimeField(verbose_name="Order Date", auto_now_add=True)
    date_of_order = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.user.username

    

    # def __str__(self):
    #     if self.user==None:
    #         return "ERROR-CUSTOMER NAME IS NULL"
    #     return self.user

#     TypeError at /admin/dashb/order/add/
# __str__ returned non-string (type datetime.datetime)
#     def __str__(self):
#         return self.date_of_order
    

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Order'
