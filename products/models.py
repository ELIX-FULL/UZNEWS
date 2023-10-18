from django.db import models

# models.py, admin.py, views.py, urls.py

class CategoryModel(models.Model):
    title = models.CharField(max_length=50)
    created_ad = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
class ProductModel(models.Model):
    title = models.CharField(max_length=50)
    category = models.ManyToManyField(CategoryModel)
    image = models.FileField(upload_to='products')
    descriptions = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'