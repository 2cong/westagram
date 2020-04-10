import json
from django.views import View
from django.http import JsonResponse, HttpResponse
from .models import Account

class AccountView(View):
     def post(self,request):
         data = json.loads(request.body)
         if Account.objects.filter(email=data['email']).exists():

             return JsonResponse({"message":"no"},status=401)
         else :
            Account.objects.create(
                 name = data['name'],
                email = data['email'],
                 password = data['password']
            )
            return HttpResponse(status=200 )

class LoginView(View):
    def post(self,request):
        data = json.loads(request.body)
        password = data['password']
        if Account.objects.filter(email=data['email']).exists():
            if Account.objects.get(email=data['email']).password == password:
               return HttpResponse(status=200)
            else :
                return JsonResponse({"message":"INVALID_USER"},status=401)
        else :
            return JsonResponse({"message":"INVALI_USER"}, status=401)
