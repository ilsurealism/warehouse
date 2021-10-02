from django.db import models
import shortuuid


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Категория')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, verbose_name='Производитель')

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'

    def __str__(self):
        return self.name


class Product(models.Model):
    code = models.CharField(primary_key=True, default=shortuuid.ShortUUID().random(8), editable=False, max_length=8, unique=True, verbose_name='Код товара')
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.PROTECT)
    manufacturer = models.ForeignKey(Manufacturer, verbose_name='Производитель', on_delete=models.PROTECT, related_name='products')
    quantity = models.PositiveIntegerField(verbose_name='Количество')
    price = models.PositiveIntegerField(verbose_name='Цена')
    created_date = models.DateField(auto_now_add=True, verbose_name='Дата добавления')
    updated_date = models.DateField(auto_now=True, verbose_name='Дата изменения')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.code
