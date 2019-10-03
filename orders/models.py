from django.db import models

# Create your models here.
class PizzaT(models.Model):
    TOPPING = (
        ('PE', 'Pepperoni'),
        ('SA', 'Sausage'),
        ('MU', 'Mushrooms'),
        ('ON', 'Onions'),
        ('HA', 'Ham'),
        ('CA', 'Canadian Bacon'),
        ('PI', 'Pineapple'),
        ('EG', 'Eggplant'),
        ('TO', 'Tomato & Basil'),
        ('GR', 'Green Peppers'),
        ('HM', 'Hamburger'),
        ('SP', 'Spinach'),
        ('AR', 'Artichoke'),
        ('BU', 'Buffalo Chicken'),
        ('BA', 'Barbecue Chicken'),
        ('AN', 'Anchovies'),
        ('BL', 'Black Olives'),
        ('FR', 'Fresh Garlic'),
        ('ZU', 'Zucchini')
    )
    topping = models.CharField(max_length=2, choices=TOPPING)

    def __str__(self):
        return f"{self.topping}"


class SubT(models.Model):
    TOPPING = (
        ('P', 'Mushrooms'),
        ('G', 'Green Peppers'),
        ('O', 'Onions')
    )
    topping = models.CharField(max_length=1, choices=TOPPING)

    def __str__(self):
        return f"{self.topping}"


class Product(models.Model):
    product = models.CharField(max_length=48)
    SIZE = (
        ('L', 'Large'),
        ('S', 'Small'),
        ('N', 'None')
    )
    size = models.CharField(max_length=1, choices=SIZE)
    pizza_toppings = models.ManyToManyField(PizzaT, blank=True, related_name="pizza_toppings")
    sub_toppings = models.ManyToManyField(SubT, blank=True, related_name="sub_toppings")
    cheese = models.BooleanField()
    topping_ct = models.IntegerField()
    price = models.FloatField()

    def __str__(self):
        return f"{self.product} {self.price}"


class Order(models.Model):
    products = models.ManyToManyField(Product, blank=True, related_name="products")
    date = models.DateField(auto_now=True)
    username = models.CharField(max_length=48)

    def __str__(self):
        return f"{self.username} {self.products} {self.date}"





