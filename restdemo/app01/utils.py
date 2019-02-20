#coding:utf-8
from rest_framework import exceptions

from rest_framework.authentication import BaseAuthentication

from .models import *


class TokenAuth(BaseAuthentication):
    def authenticate(self, request):
        token = request.GET.get("token")
        token_obj = Token.objects.filter(token=token).first()
        if not token_obj:
            raise exceptions.AuthenticationFailed("请先联系管理员授权!")
        else:
            return token_obj.user.name, token_obj.token

