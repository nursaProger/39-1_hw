from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Review(models.Model):
    text = models.TextField(null=True, blank=True)
    stars = models.IntegerField(default=1, choices=[(i, i) for i in range(1, 6)])
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
