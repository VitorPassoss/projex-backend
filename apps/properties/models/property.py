from django.db import models
from django.contrib.auth.models import User

PROPERTY_TYPE = [
    ("C","Casa"),
    ("A", "Apartamento"),
    ("T", "Terreno")
]


class Property(models.Model):
    user_fk = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    property_type = models.CharField(
        max_length=2, choices=PROPERTY_TYPE, blank=True
    )
    adress = models.CharField(
        max_length=255
    )
    price = models.DecimalField(max_digits=19, decimal_places=2)
    price_buyer = models.DecimalField(max_digits=19, decimal_places=2)
    price_seller = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True,default=0)
    size = models.DecimalField(max_digits=19, decimal_places=2)
    bedrooms = models.DecimalField(max_digits=19, decimal_places=0)
    availability = models.BooleanField(default=True)
    image_url = models.CharField(
        max_length=255
    )# Diretório onde as imagens serão salvas.
