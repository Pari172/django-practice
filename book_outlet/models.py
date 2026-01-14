from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=2)

class Address(models.Model):
    street = models.CharField(max_length=20)
    postal_code = models.CharField(max_length=6)
    city = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.street}, pin-{self.postal_code}, {self.city}"
    class Meta:
        # ordering = ['price']  # Sort by price ascending
        verbose_name = "Address"
        verbose_name_plural = "Addresses"

class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    address = models.OneToOneField(
        Address, on_delete=models.CASCADE,null=True
    )
    def __str__(self):
        return self.first_name+self.last_name

class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    # author = models.CharField(null=True, max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE,null=True,related_name='books')
    published_countries = models.ManyToManyField(Country,null=True)
    is_bestselling = models.BooleanField(default= False)
    slug = models.SlugField(default="",null=False)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse("book-details", args=[self.slug])
    

    def __str__(self):
        return f"{self.title} - {self.rating}"