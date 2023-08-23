from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name

# model for nested serializer
class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    book_name = models.CharField(max_length=100)