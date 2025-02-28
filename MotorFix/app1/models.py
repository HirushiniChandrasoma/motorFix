from django.db import models

class CarParts(models.Model):
    CAR_PART_TYPES = [
        ("Engine", "Engine"),
        ("Brakes", "Brakes"),
        ("Battery", "Battery"),
        ("Transmission", "Transmission"),
        ("Suspension", "Suspension"),
        ("Exhaust", "Exhaust"),
        ("Lights", "Lights"),
        ("Tires", "Tires"),
    ]

    itemId = models.CharField(max_length=8, unique=True)
    itemName = models.CharField(max_length=200)
    itemType = models.CharField(max_length=20, choices=CAR_PART_TYPES)
    itemDescription = models.CharField(max_length=150)
    itemPrice = models.FloatField(max_length=10)
    itemImage = models.ImageField(upload_to='car_parts/', null=True, blank=True)

    class Meta:
        db_table = "CarParts"
