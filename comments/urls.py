from django.urls import path
from .views import CommentView, MyReplyView

urlpatterns = [
    path('reply',CommentView.as_view()),
    path('myreply/<str:address>',MyReplyView.as_view()),
]
