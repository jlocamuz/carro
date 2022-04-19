
from multiprocessing.connection import Client
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from sqlalchemy import null, true
import datetime

class MyUserManager(BaseUserManager):
    def create_user(self, name, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            name=name,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, email,password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            name, 
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    name = models.CharField(max_length=30, unique=True)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = ['email'] # lo q preguntara en createsuperuser sumando password y usernamefiel


    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    # is stuff =  is admin
    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    


class ClientDetail(models.Model):
    client_address = models.CharField(max_length=50)
    client_phone = models.IntegerField()
    client = models.ForeignKey(User, on_delete=models.CASCADE)


class ShoppingCart(models.Model): 
    client_detail = models.ForeignKey(ClientDetail, on_delete=models.CASCADE) #client
    sc_total_price = models.FloatField(default=0)

# se crea cuando apretamos un 'agregar al carrito'
class CartDetail(models.Model):
    sc = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)
    product = models.CharField(max_length=50)
    product_quantity = models.IntegerField()

class Sale(models.Model):
    client_detail = models.ForeignKey(ClientDetail,  on_delete=models.CASCADE)
    sale_date = models.DateField(default=datetime.date.today)


class SaleDetail(models.Model):
    sale = models.ForeignKey(Sale,  on_delete=models.CASCADE) 
    product = models.CharField(max_length=50)
    product_quantity = models.IntegerField()