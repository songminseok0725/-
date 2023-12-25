from rest_framework import serializers
from .models import Deposite_baselist, Deposite_optionlist, Saving_baselist, Saving_optionlist, Bank

class Deposite_baselistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposite_baselist
        fields = '__all__'

class Deposite_optionlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposite_optionlist
        exclude = ('base',)

class Saving_baselistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saving_baselist
        fields = '__all__'

class Saving_optionlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saving_optionlist
        exclude = ('base',)

class BanklistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = '__all__'

class DepositeListSerializer(serializers.ModelSerializer):
    deposite_optionlist_set = Deposite_optionlistSerializer(many=True, read_only=True)
    class Meta:
        model = Deposite_baselist
        fields = '__all__'

class SavingListSerializer(serializers.ModelSerializer):
    saving_optionlist_set = Saving_optionlistSerializer(many=True, read_only=True)
    class Meta:
        model = Saving_baselist
        fields = '__all__'