from django.contrib.auth.models import AbstractUser
from django.db import models


class Publication(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)

    class Meta:
        ordering = ['headline']

    def __str__(self):
        return self.headline


class MyUser(AbstractUser):
    birth_date = models.DateField(null=True)
    avatar = models.ImageField(blank=True, null=True)


class Customer(models.Model):
    name = models.CharField(max_length=120)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class CustomerSettings(models.Model):
    preferred_color = models.CharField(max_length=120)
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, related_name='cus')

    def __str__(self):
        return f"{self.customer.name} - {self.preferred_color}"


class Author(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=120)
    year_of_public = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return f"{self.name} - {self.author.name}"
