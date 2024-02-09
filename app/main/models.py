from django.db import models

# Create your models here.

class ProductSize(models.Model):
    type = models.CharField(max_length = 30)

    def __str__(self):
        return self.type

class Intro(models.Model):
    name = models.CharField(max_length = 30)
    quote = models.CharField(max_length = 60) 
    discription = models.TextField()

    class Meta:
        verbose_name = 'Intro'
        verbose_name_plural = 'Intro'

    def __str__(self):
        return self.name
    
class Product(models.Model):
    img = models.ImageField(upload_to = 'images/product/')
    name = models.CharField(max_length = 30)
    size = models.ManyToManyField(ProductSize)
    PriceSmall = models.FloatField()
    PriceMiddle = models.FloatField()
    PriceLarge = models.FloatField()

    def __str__(self):
        return self.name
    
class About(models.Model):
    title = models.CharField(max_length = 30)
    text = models.TextField()

    class Meta:
        verbose_name = "About"
        verbose_name_plural = "About"

    def __str__(self):
        return self.title
    
class ContactUsInfo(models.Model):
    text = models.TextField()
    phone = models.CharField(max_length = 20)
    email = models.EmailField()
    location = models.URLField()

    class Meta:
        verbose_name = "Contact Us info"
        verbose_name_plural = "Contact Us info"

    def __str__(self):
        return 'ContactUs banner info'
    
class ContactUsUser(models.Model):
    name = models.CharField(max_length = 50)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
    
