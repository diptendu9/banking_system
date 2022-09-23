from rest_framework import generics
from banking.models import Accholder
from banking.serializer import BankingSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.renderers import TemplateHTMLRenderer
from django.shortcuts import redirect,render, get_object_or_404
from .forms import CreateAccountForm
from django.contrib.auth.models import User


# Create your views here.


class AccUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset= Accholder.objects.all()
    serializer_class= BankingSerializer

class CreateAccount(generics.CreateAPIView):
    
    serializer_class = BankingSerializer
    permission_classes = [IsAuthenticated]
    renderer_classes =[TemplateHTMLRenderer]
    template_name = 'accn.html'
    queryset = Accholder.objects.all()

    # print("hwehkqedjkqsjaxjksa")
    def get(self, request):
        # profile = get_object_or_404(Accholder)

        serializer = BankingSerializer()
        form = CreateAccountForm()
        return Response({'serializer': serializer,'form':form})

    def post(self, request):
        import ipdb; ipdb.set_trace()
        form = CreateAccountForm(request.POST)
        print(form.is_valid())
        serializer = BankingSerializer()
        print(request.POST)
        
        if form.is_valid():
            form.save()
           
            return redirect('home')
        return Response({'serializer': serializer,'form':form})
    # def post(self,request,pk):
    #     profile = get_object_or_404(Accholder, pk=pk)
    #     serial = BankingSerializer(data = request.data, many=True)
    #     print(serial)
        
    #     if serial.is_valid():
    #         serial.save()
    #     return HTTPResponse('banking')


class ViewAccount(generics.ListAPIView):
    serializer_class = BankingSerializer

    def get_queryset(self):
        logged_in_user = self.request.user.id
        queryset = Accholder.objects.filter(id = logged_in_user)
        return queryset



@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def GetUserBalance(request):
    # def get_queryset(self):
        user_id= request.user.id
        return Response(Accholder.objects.filter(user__id=user_id).first().balance)

    # content = {
    #     'balance': str(Accholder.balance)
    # }
    # return Response(content)

class TransactionAPIview(generics.CreateAPIView):
    renderer_classes =TemplateHTMLRenderer
    serializer_class= BankingSerializer
    template_name='index.html'
