from django.db import models

class Book(models.Model):
    ISBN = models.CharField(max_length = 10, primary_key = True)
    Title = models.CharField(max_length = 200)
    AuthorID = models.CharField(max_length = 10)
    Publisher = models.CharField(max_length = 30)
    PublishDate = models.DateField()
    Price = models.FloatField()


class Author(models.Model):
    AuthorID = models.CharField(max_length = 10, primary_key = True)
    Name = models.CharField(max_length = 30)
    Age = models.IntegerField()
    Country = models.CharField(max_length = 50)

# Create your models here.
