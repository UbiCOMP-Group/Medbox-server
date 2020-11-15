from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from DeviceAPI.serializers import DeviceSerializer
from DeviceAPI.models import Device


class DeviceList(generics.ListCreateAPIView):
    """Endpoint for managing devices."""
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request):
        queryset = self.get_queryset()
        queryset = queryset.filter(owner=request.user)
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)


class DeviceDetail(generics.RetrieveUpdateDestroyAPIView):
    """Endpoint for managing devices."""
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [IsAuthenticated]


# still work to do


class DevicePairing(generics.RetrieveUpdateDestroyAPIView):
    """Endpoint for pairing device"""
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


    def get(self, request):
        """gets current pairing code from server"""
        queryset = self.get_queryset()
        code = queryset.pairing_code
        context = {
            "pairing_code": code,
        }
        return Response(context)  # should be json format; how to test it?
