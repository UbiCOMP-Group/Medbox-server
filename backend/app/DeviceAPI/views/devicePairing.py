from DeviceAPI.serializers import PairingInfoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from DeviceAPI.models import Device, PairingInfo


class PairingInfoCreate(APIView):
    """Endpoint for creating PairingInfo object"""

    def post(self, request):
        request.data["pairing_code"] = PairingInfo.generate_code()
        serializer = PairingInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            pairing_info = serializer.save()
            return Response(data={"pairing_code": pairing_info.pairing_code})
        else:
            return Response(serializer.errors)


class PairingConfirmCode(APIView):
    """Endpoint for pairing by code"""
    queryset = Device.objects.all()

    def get(self, request, pk):
        pass
             
"""        try:
            code = user.PairingInfo.pairing_code
            if(code == pk)
                api_token = Token.objects.get(user = user)
                data = { "Token": api_token.key}
                return Response(data)
            else:
                return Response(status = status.HTTP_401_UNAUTHORIZED)
        except: 
            return Response(status = status.HTTP_403_FORBIDDEN) 
        try:
            code = user.PairingInfo.pairing_code
        except:
            return Response(status = status.HTTP_401_UNAUTHORIZED)
        else:
            if(code == pk):
                api_token = Token.objects.get(user = user)
                data = { "Token": api_token.key} """
        