import email
from rest_framework import generics, status
from banking.models import Accholder, Transactions, Transfers
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
        account = get_object_or_404(Accholder,user=request.user)
        form = TransactionForm()
        return Response({'seializer': seralizer, 'form': form, "account" : account})

    def post(self, request):
        account = get_object_or_404(Accholder,user=request.user)
        print(account.name)
        serializer = TranasctionSerializer(data=request.data)
        form = TransactionForm(request.POST)
        form_dict = form.data.dict()
        form = TransactionForm(form_dict)
        print(form.data)
        print(form.is_valid())
        if form.is_valid():
            print(account.balance)
            trans_type = form.cleaned_data['t_type']
            amount = form.cleaned_data['amount']
            print(trans_type)

            if(trans_type == 'Withdrawn') :
                
                if(amount>account.balance) :
                    return HttpResponse("Balance is low")
                else:
                    account.balance=account.balance-amount
                    account.save()
            elif(trans_type == 'Deposited') :
                account.balance=account.balance+amount
                account.save()
            form.instance.user= account
            form.save()
            return redirect('home')
        return Response({'serializer': serializer,'form':form})


class TransferAPIView(generics.CreateAPIView) :
    renderer_classes = [TemplateHTMLRenderer]
    permission_classes = [IsAuthenticated]
    template_name = "transfer.html"
    serializer_class = TransferSerializer
    queryset = Transfers.objects.all()

    def get(self, request) :
        serializer = TransferSerializer()
        form = TransferForm()
        account = get_object_or_404(Accholder,user=request.user)
        return Response({'seializer': serializer, 'form': form, "account" : account})

    # def post(self, request):
    #     account = get_object_or_404(Accholder,user=request.user)
    #     print(account.name)
    #     serializer = TransferSerializer(data=request.data)
    #     form = TransferForm(request.POST)
    #     form_dict = form.data.dict()
    #     form = TransferForm(form_dict)
    #     print(form.data)
    #     print(form.is_valid())
    #     if form.is_valid():
    #         print(account.balance)
    #         trans_type = form.cleaned_data['t_type']
    #         amount = form.cleaned_data['amount']
    #         print(trans_type)

    #         if(trans_type == 'Withdrawn') :
                
    #             if(amount>account.balance) :
    #                 return HttpResponse("Balance is low")
    #             else:
    #                 account.balance=account.balance-amount
    #                 account.save()
    #         elif(trans_type == 'Deposited') :
    #             account.balance=account.balance+amount
    #             account.save()
    #         form.instance.user= account
    #         form.save()
    #         return redirect('home')
    #     return Response({'serializer': serializer,'form':form})

    def post(self,request):
        # import ipdb; ipdb.set_trace()

        serializer = TransferSerializer(data=request.data)
        account = get_object_or_404(Accholder,user=request.user)
        print(account.name)
        
        form = TransferForm(request.POST)
        print(form.data)
        form_dict = form.data.dict()
        form = TransferForm(form_dict)
        print(form.data)
        print(form.is_valid())
        if form.is_valid():
            amount =form.cleaned_data['amount']
            reciver = form.cleaned_data['reciver']
            if account.balance > amount:
                    account.balance -= amount
                    account.save()
                    receiver = Accholder.objects.get(account_number=reciver)
                    print(reciver)
                    receiver.balance += amount
                    receiver.save()
                    form.instance.user= account
                    form.save()
            else :
                return HttpResponse("Balance is low")

            return redirect('home')
        return Response({'serializer': serializer,'form':form, "account" : account})






    
