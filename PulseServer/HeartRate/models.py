from django.db import models


# Create your models here.

class PulseValue(models.Model):
    value = models.IntegerField(default=60)

    def update_value(self, val: int):
        self.value = val

    def __str__(self):
        return self.value
