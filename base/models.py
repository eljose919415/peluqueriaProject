from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class BaseModel(models.Model):
    status = models.BooleanField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BaseModelNameAbv(BaseModel):
    name = models.CharField(max_length=200, unique=True)
    abv = models.CharField(max_length=10, unique=True)

    class Meta:
        ordering = ["name"]
        unique_together = ("name", "abv")
        abstract = True


class BaseModelNameDescription(BaseModel):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()

    class Meta:
        ordering = ["name"]
        unique_together = ("name", "description")
        abstract = True


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    phone_number = models.PositiveIntegerField(null=True, blank=True)


class Currency(BaseModelNameAbv):
    places = models.PositiveIntegerField()

    def save(self, **kwargs):
        self.name = self.name.capitalize()
        self.abv = self.abv.upper()
        super(Currency, self).save()

    def __str__(self):
        return f"{self.name}-{self.abv}"


class ServicesAvailable(BaseModelNameDescription):
    def save(self, **kwargs):
        self.name = self.name.capitalize()
        super(ServicesAvailable, self).save()

    def __str__(self):
        return self.name


class ProductsAvailable(BaseModelNameDescription):
    def save(self, **kwargs):
        self.name = self.name.capitalize()
        super(ProductsAvailable, self).save()

    def __str__(self):
        return self.name


class ImagesManage(BaseModelNameDescription):
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.name
