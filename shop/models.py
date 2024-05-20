from django.db import models
from django.utils.text import slugify
from django.urls import reverse

import random, string


def rand_slug():
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(3))


class Category(models.Model):
    name = models.CharField('Название', max_length=250)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children',
                               verbose_name='Родительская категория', blank=True, null=True)
    slug = models.SlugField('URL', max_length=250, unique=True, editable=True)
    created_at = models.DateTimeField('Создание', auto_now_add=True)

    class Meta:
        unique_together = (['parent', 'slug'])
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        full_path = [self.name]
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return ' -> '.join(full_path[::-1])
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(rand_slug() + '-pickBetter' + self.name)
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('shop:category-list', args=[str(self.slug)])

    
class Product(models.Model):
    title = models.CharField('Название', max_length=250)
    description = models.TextField('Описание', max_length=1000, blank=True)
    brand = models.CharField('Бренд', max_length=250, blank=True)
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE,
                                 related_name='products')
    slug = models.SlugField('URL', max_length=250, unique=True, editable=True)
    price = models.DecimalField('Цена', max_digits=7, decimal_places=2, default=99.99)
    image = models.ImageField('Изображение', upload_to='products/products/%Y/%m/%d')
    available = models.BooleanField('Наличие', default=True)
    created_at = models.DateTimeField('Создание', auto_now_add=True)
    updated_at = models.DateTimeField('Изменено', auto_now=True)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('shop:products-detail', args=[str(self.slug)])


class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(available=True)

    
class ProductProxy(Product):
    objects = ProductManager()

    class Meta:
        proxy = True
        

