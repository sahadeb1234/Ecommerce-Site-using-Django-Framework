from django.contrib.auth.models import User
from authentication import views
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200, null=True, blank=True)
    joined_on= models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return  self.full_name

class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def __str__(self) -> str:
        return self.title

class Product(models.Model):
    title= models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    Category= models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="products")
    marked_price = models.PositiveIntegerField()
    selling_price = models.PositiveIntegerField()
    description = models.TextField()
    warranty = models.CharField(max_length=300, null=True, blank=True)
    return_policy = models.CharField(max_length=300, null=True, blank=True)
    views_count = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return self.title


class Cart(models.Model):
    Customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    total = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "cart: " +str(self.id)


class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    Product = models.ForeignKey(Product, models.CASCADE)
    rate = models.PositiveIntegerField()
    quantity = models.PositiveBigIntegerField()
    subtotal = models.PositiveIntegerField()

def __str__(self):
        return "Cart: " +str(self.Cart.id) + "CartProduct: " + str (self.id)

ORDER_STATUS =(
("Order Received","Order Received" ), 
("Order Processing","Order Processing" ), 
("On the way", "On the way"),
("Order Canceled", "Order Canceled"),

)

class Order(models.Model):
     Cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
     order_by = models.CharField(max_length=200)
     shipping_address = models.CharField(max_length=200)
     mobiles = models.CharField(max_length=10)
     email = models.EmailField(null=True, blank=True)
     subtotal = models.PositiveIntegerField()
     discount = models.PositiveIntegerField
     total = models.PositiveIntegerField()
     oder_status = models.CharField(max_length=50, choices=ORDER_STATUS)
     created_at = models.DateTimeField(auto_now_add=True)


     def __str__(self): 
         return "Order: " +str(self.id)




    




