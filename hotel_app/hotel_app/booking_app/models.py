from datetime import datetime

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Room(models.Model):
    number = models.CharField(max_length=5)
    cost = models.IntegerField()
    beds_count = models.IntegerField()

    def __str__(self):
        return self.number + ', кол-во мест: ' + str(self.beds_count) \
               + ', стоимость в сутки: ' + str(self.cost)

class Booking(models.Model):
    date_start = models.DateField(default=datetime.now)
    date_finish = models.DateField(default=datetime.now)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)
