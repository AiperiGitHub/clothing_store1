from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True, default=None)
    image = models.ImageField(upload_to='/products_images/')
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = "фотография"
        verbose_name_plural = "фотографии"






    # def __init__(self, *args, **kwargs):
    #     super().__init__(args, kwargs)
    #     self.name = None
    #
    # def Brand(self):
    #     name = models.CharField(max_length=255)     #которое будет хранить название бренда
    #     description = models.TextField()            # можете хранить дополнительную информацию о бренде
    #     logo = models.ImageField(upload_to='logos/', null=True, blank=True)  #загружать изображения логотипов бренда.
    #
    # def __str__(self):
    #     return self.name

class Subscriber:
    pass