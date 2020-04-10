import json
from django.views import View
from django.http import JsonResponse,HttpResponse
from .models import Comment
from account.models import Account

class CommentView(View):
    def post(self,request):
        data = json.loads(request.body)
        if Account.objects.filter(email=data['email']).exists():
            reply_westa = Comment(
                 email = data['email'],
                 reply = data['reply']
             )
            reply_westa.save()
            return HttpResponse(status=200)
        else :
            return JsonResponse({"message":"INVALID_USER"}, status=401)

class MyReplyView(View):
    def get(self,request,address):
        my_reply= Comment.objects.filter(email=address)
        my_reply_list=[]
        for i in range(len(my_reply)):
            my_reply_list.append(my_reply.values()[i]['reply'])
        return JsonResponse({"comment":my_reply_list},status=200)



