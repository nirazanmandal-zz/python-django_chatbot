from django.db import models
import uuid


class UserAccount(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return str(self.username)


class SessionToken(models.Model):
    username = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    token = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)
    valid = models.BooleanField(default=True)

    def create_token(self):
        self.token = uuid.uuid4()

    def __str__(self):
        return str(self.username)


