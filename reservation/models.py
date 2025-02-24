from django.db import models
from base.models import BaseModel, CustomUser


# Create your models here.
class Reservation(BaseModel):
    phone = models.PositiveIntegerField()
    reservation_date_first = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}-{self.phone}"


class ReservationHistory(models.Model):
    phone = models.PositiveIntegerField()
    email = models.EmailField(null=True, blank=True)
    person = models.CharField(max_length=250)
    reservation_date = models.DateTimeField()

    def __str__(self):
        return f"{self.person}-{self.reservation_date}"
