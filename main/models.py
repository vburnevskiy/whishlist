from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    """ Таблиуа Товары
    джанго сам добавит id

    """
    title = models.CharField(max_length=120)
    link = models.URLField()
    price = models.IntegerField()
    create_at = models.DateTimeField(auto_created=True, auto_now_add= True)
    def __str__(self):
        return self.title

class WishList(models.Model):
    """
    owner
    id
    products - ManyToMany
    """
    title = models.CharField(max_length=120)
    product = models.ManyToManyField(Product)
    is_hidden = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title


