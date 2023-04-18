from django.db import models
from django.contrib import admin

# Create your models here.
class ProductCategory(models.Model):
    """The category schema"""
    name = models.CharField('Category name', max_length=100)
    description = models.CharField('Category description', max_length=300)

class Product(models.Model):
    """The product schema the products will follow in the database"""
    name = models.CharField('Product name', max_length=200)
    image = models.CharField('Product image', max_length=300)
    stock = models.IntegerField('Product stock', default=0)
    price = models.DecimalField('Product price', max_digits=10,decimal_places=2)
    category_id = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return super().__str__()
    
    @admin.display(
        boolean = True,
        ordering='stock',
        description='Is availible?'
    )
    def is_availible(self) -> bool:
        return self.stock > 0

class Client(models.Model):
    """"""
    first_name = models.CharField('Client first name', max_length=100)
    last_name = models.CharField('Client last name', max_length=200)
    address = models.CharField('Client address', max_length=300)
    phone = models.IntegerField('Client phone')
    mail = models.CharField('Client e-mail', max_length=100)


class PaymentMethod(models.Model):
    """"""
    name = models.CharField('Payment method', max_length=100)

class Bill(models.Model):
    """"""
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    date = models.DateTimeField('Sell date', auto_now=True)
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE)

class BillDetails(models.Model):
    """"""
    bill_id = models.ForeignKey(Bill, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField('Product quantity')

    @admin.display(
        boolean = False,
        ordering='quantity',
        description='Final price',
    )
    def sale_price(self) -> int:
        return self.product_id.price * self.quantity