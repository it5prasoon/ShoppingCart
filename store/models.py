from django.db import models
from django.urls import reverse

colour_choices = (('Blue', 'Blue'), ('Green', 'Green'), ('Black', 'Black'), ('Red', 'Red'))
size_choices = (
    ('S', 'S'),
    ('M', 'M'),
    ('L', 'L'),
    ('XL', 'XL'),
    ('XXL', 'XXL'),
    ('XXXL', 'XXXL')
)


# Design of Product
class Category(models.Model):
    name = models.CharField(max_length=300, unique=True)
    slug = models.SlugField(max_length=300, unique=True)
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
    name = models.CharField(max_length=300, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField()
    stock = models.IntegerField()
    color = models.CharField(max_length=20, choices=colour_choices, default='L')
    size = models.CharField(max_length=20, choices=size_choices, default='3')
    image = models.ImageField(upload_to='product', blank=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Product'
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def get_url(self):
        return reverse('store:ProdCatDetail', args=[self.category.slug, self.slug])

    def __str__(self):
        return '{}'.format(self.name)


class VariationColor(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.CharField(max_length=120)
    image = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE, related_name='images')
    price = models.DecimalField(decimal_places=2, max_digits=100, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.color

class VariationSize(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.CharField(max_length=120)
    image = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE, related_name='image1')
    price = models.DecimalField(decimal_places=2, max_digits=100, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.size