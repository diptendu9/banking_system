from urllib import response
from rest_framework import generics
from banking.models import Accholder
from banking.serializer import BankingSerializer
from rest_framework.response import Response
# Create your views here.


class CreateAccount(generics.CreateAPIView):

    serializer_class = BankingSerializer    
    def post(self,request):
        serial = BankingSerializer(data = request.data)
        print(serial)
        if serial.is_valid():
            serial.save()
        return Response(
            {
                'status': "Pass",
                'data': serial.data
            }
        )


