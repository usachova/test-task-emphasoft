from django.db import models

# Create your models here.
class Room(models.Model):
    number = models.CharField(max_length=5)
    cost = models.IntegerField()
    beds_count = models.IntegerField()

    def __str__(self):
        return self.number
