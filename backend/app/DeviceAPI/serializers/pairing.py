from rest_framework import serializers
from DeviceAPI.models import PairingInfo


class PairingInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = PairingInfo
        fields = [
            "pairing_code",
            "serial_number",
            "hardware_version",
            "firmware_version",
        ]
