from rest_framework import serializers
from allauth.account import app_settings as allauth_settings
from allauth.utils import get_username_max_length
from allauth.account.adapter import get_adapter
from django.contrib.auth import get_user_model

from .models import User
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import UserDetailsSerializer


class CustomRegisterSerializer(RegisterSerializer):
# 추가할 필드들을 정의합니다.
#     nickname = serializers.CharField(
# required=False,
# allow_blank=True,
# max_length=255
# )
    age = serializers.IntegerField(required=False)
    money = serializers.IntegerField(required=False)
    salary = serializers.IntegerField(required=False)
    financial_products = serializers.CharField(required=False)
    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'nickname': self.validated_data.get('nickname', ''),
            'age': self.validated_data.get('age', ''),
            'money': self.validated_data.get('money', ''),
            'salary': self.validated_data.get('salary', ''),
            'financial_products': self.validated_data.get('financial_products', ''),
        }
    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        self.custom_signup(request, user)
        return user
    

class CustomUserDetailsSerializer(UserDetailsSerializer):

    # nickname = serializers.CharField(
    #     required=False,
    #     allow_blank=True,
    #     max_length=255
    # )
    financial_products = serializers.CharField(required=False)

    class Meta:
        model = get_user_model()
        fields = UserDetailsSerializer.Meta.fields + ('age', 'nickname', 'salary', 'money', 'financial_products')
        read_only_fields = ('username',)


    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        # data['username'] = self.validated_data.get('username', '')
        if(self.validated_data.get('age',  None)):
            data['age'] = self.validated_data.get('age',  None)
        if(self.validated_data.get('nickname', '')):
            data['nickname'] = self.validated_data.get('nickname', '')
        if(self.validated_data.get('salary', None)):
            data['salary'] = self.validated_data.get('salary', None)
        if(self.validated_data.get('money',  None)):
            data['money'] = self.validated_data.get('money',  None)
        if(self.validated_data.get('financial_products', '')):
            data['financial_products'] = self.validated_data.get('financial_products', '')
        if(self.validated_data.get('email','')):
            data['email'] = self.validated_data.get('email','')
        return data
    
    def update(self, instance, validated_data):
        print('update')
        instance = super().update(instance, validated_data)
        # instance.username = validated_data.get('username', '')
        if(validated_data.get('age', None)):
            instance.age = validated_data.get('age', None)
        if(validated_data.get('nickname', '')):
            instance.nickname = validated_data.get('nickname', '')
        if(validated_data.get('salary', None)):
            instance.salary = validated_data.get('salary', None)
        if(validated_data.get('money', None)):
            instance.money = validated_data.get('money', None)
        if(validated_data.get('financial_products', '')):
            instance.financial_products = validated_data.get('financial_products', '')
        if(validated_data.get('email','')):
            instance.email = validated_data.get('email','')
        instance.save()
        return instance
    

    def save(self):
        self.validated_data.pop('username', None)
        user = super().save()
        if(self.validated_data.get('age', None)):
            user.age = self.validated_data.get('age', None)
        if(self.validated_data.get('nickname', '')):
            user.nickname = self.validated_data.get('nickname', '')
        if(self.validated_data.get('salary', None)):
            user.salary = self.validated_data.get('salary', None)
        if(self.validated_data.get('money', None)):
            user.money = self.validated_data.get('money', None)
        if(self.validated_data.get('financial_products', '')):
            user.financial_products = self.validated_data.get('financial_products', '')
        if(self.validated_data.get('email','')):
            user.email = self.validated_data.get('email','')
        user.save()
        return user