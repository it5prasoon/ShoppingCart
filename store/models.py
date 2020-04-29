from django.db import models
from django.urls import reverse


# Design of Product
class Category(models.Model):
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=300)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='category', blank=True)

    class META:
        db_table = 'Category'
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('store:products_by_category', args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)


# Product Model
class Product(models.Model):
    image = models.ImageField(upload_to='store/', blank=True)
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=250)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField()
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Product'
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def get_url(self):
        return reverse('store:ProdCartDetail', args=[self.category.slug, self.slug])

    def __str__(self):
        return '{}'.format(self.name)
