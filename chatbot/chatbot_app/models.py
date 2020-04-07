from django.db import models
from account_app.models import UserAccount


class Chat(models.Model):
    # name = models.ForeignKey(UserAccount, default='', null=True, on_delete=models.CASCADE)
    # username = models.CharField(max_length=100, default='')
    message = models.CharField(max_length=100, default='')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.message)
