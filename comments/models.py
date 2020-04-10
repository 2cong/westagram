from django.db import models

class Comment(models.Model):
    email = models.CharField(max_length=200)
    reply = models.TextField()
    crated_reply = models.DateTimeField(auto_now_add=True)
    updated_reply = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "comments"

