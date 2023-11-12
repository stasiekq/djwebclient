from django.db import models

class Booking(models.Model):
    id = models.CharField(max_length=20)
    guestName = models.CharField(max_length=100)
    roomNumber = models.CharField(max_length=10)

    def __str__(self):
        return self.name