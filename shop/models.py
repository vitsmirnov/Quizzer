from django.db import models


class Color(models.Model):
    name = models.CharField(verbose_name='Color name', default='', unique=True,
                            max_length=32)
    value = models.CharField(default='rgba(255,255,255,1)', max_length=64)  # unique=?
    price = models.IntegerField(default=0)
    # description = models.CharField(default='', max_length=512)

    def __str__(self) -> str:
        return f"Color: {self.name} ({self.value}), price: {self.price}"
