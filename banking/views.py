import email
from rest_framework import generics, status
from banking.models import Accholder, Transactions
from banking.serializer import BankingSerializer, TranasctionSerializer, TransferSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.renderers import TemplateHTMLRenderer
from django.shortcuts import redirect,render, get_object_or_404
from .forms import CreateAccountForm, TransactionForm, TransferForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.db.models import F

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
        # import ipdb; ipdb.set_trace()
        form = CreateAccountForm(request.POST)
        serializer = BankingSerializer(data = request.data)
        
        form_dict = form.data.dict()
    
        form_dict['user']= request.user
        form = CreateAccountForm(form_dict)
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
    # import ipdb; ipdb.set_trace()
    renderer_classes =[TemplateHTMLRenderer]
    permission_classes = [IsAuthenticated]
    serializer_class= TranasctionSerializer
    template_name='index.html'
    queryset = Transactions.objects.all()

    # queryset = Transactions.objects.all()



    def get(self,request):
        seralizer = TranasctionSerializer()
        form = TransactionForm
        return Response({'seializer': seralizer, 'form': form})

    def post(self, request):
        account = get_object_or_404(Accholder,user=request.user)
        serializer = TranasctionSerializer()
        form = TransactionForm(request.POST)
        if form.is_valid():
            t_type = serializer.validated_data.get('t_type')
            amount = serializer.validated_data.get('amount')
            if(t_type == 'Withdraw') :
                if(amount>account.balance) :
                    return HttpResponse("Balance is low")
                else:
                    account.balance=account.balance-amount
                    account.save()
            elif(t_type == 'Deposit') :
                account.balance=account.balance+amount
                print(account.balance)
                account.save()
            form.save()
            return redirect('home')
        return Response(status=status.HTTP_400_BAD_REQUEST)


class TransferAPIView(generics.CreateAPIView) :
    renderer_classes = [TemplateHTMLRenderer]
    permission_classes = [IsAuthenticated]

    template_name = "transfer.html"
    serializer_class = TransferSerializer

    def get(self, request) :
        serializer = TransferSerializer()
        form = TransferForm
        return Response({'serializer' : serializer,'form' : form})

    def post(self,request,*args,**kwargs):
        serializer = TransferSerializer(data=request.data)
        if serializer.is_valid() :
            amount =serializer.validated_data.get('amount')
            to_account = serializer.validated_data.get('reciver')
            sender = get_object_or_404(Accholder,user=request.user)
        if sender.balance > amount:
            # debit the sender account
                sender.balance -= amount
                sender.save()
            #credit the receiver account
                receiver = Accholder.objects.get(account_number=to_account)
                receiver.balance += amount
                receiver.save()
                serializer.save()
        else :
            return HttpResponse("Balance is low")
        return HttpResponse("Done")






    
