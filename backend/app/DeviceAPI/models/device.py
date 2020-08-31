"""
Device model.
"""

__author__ = "Krzysztof Adamkiewicz"
__status__ = "development"
__date__ = "25.5.2020"

from django.db import models
from django.contrib.auth import get_user_model
import uuid as UUID

class Device(models.Model):
    """
    Model of the device.
    """
    # universal identifier
    uuid = models.UUIDField(primary_key=True, default=UUID.uuid4, editable=False, unique=True)
    
    # name given to the device by user
    name = models.CharField(max_length=100, blank=True, default='')
    
    # users to which the device is assigned
    users = models.ManyToManyField(get_user_model())

    # pairing key used to connect the device with a user's account
    pairingKey = models.CharField(max_length=6, default='')

    # pairing key expiration date
    pairingKeyExpiresAt = models.DateTimeField(null=True)

    # token used to authenticated API calls from this device
    apiToken = models.CharField(max_length=42, default='')

    # containers mounted to this box
    containers = models.ManyToManyField("Container")

    def __str__(self):
        return f"'{self.name}' with id: {self.uuid}"
