from urllib import response
from rest_framework import generics
from banking.models import Accholder
from banking.serializer import BankingSerializer
from rest_framework.response import Response
from rest_framework import permissions
# Create your views here.



class CreateAccount(generics.CreateAPIView):

    serializer_class = BankingSerializer    

    # def get(self,request):

    # def get(self, request):
    #     u= Accholder.objects.all()
    #     serial = BankingSerializer(data=u, many=True)
    #     return Response(serial.data())

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


class ViewAccount(generics.ListAPIView):
    serializer_class = BankingSerializer

    def get_queryset(self):
        logged_in_user = self.request.user.id
        queryset = Accholder.objects.filter(id = logged_in_user)
        return queryset