import requests
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import Deposite_baselistSerializer, Deposite_optionlistSerializer, Saving_baselistSerializer, Saving_optionlistSerializer, BanklistSerializer, DepositeListSerializer, SavingListSerializer
from .models import Deposite_baselist, Deposite_optionlist, Saving_baselist, Saving_optionlist, Bank
from accounts.models import User
from accounts.serializers import CustomUserDetailsSerializer, CustomRegisterSerializer
from django.db.models import Q

@api_view(['GET'])
def index(request):

    # 정기예금 
    api_key = settings.API_KEY_PRODUCTS
    now_number = 1
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo={1}'
    response = requests.get(url).json()
    max_number = response['result']['max_page_no']
    for base in response ["result"] ["baseList"] :
        is_saved = Deposite_baselist.objects.filter(fin_prdt_cd=base["fin_prdt_cd"])
        if not is_saved:
            serializer = Deposite_baselistSerializer(data=base)
            if serializer.is_valid():
                serializer.save()
    while(now_number != max_number):
        now_number += 1
        url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo={now_number}    '
        response = requests.get(url).json()
        for base in response ["result"] ["baseList"] :
            is_saved = Deposite_baselist.objects.filter(fin_prdt_cd=base["fin_prdt_cd"])
            if not is_saved:
                serializer = Deposite_baselistSerializer(data=base)
                if serializer.is_valid():
                    serializer.save()
    now_number = 1
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo={1}'
    response = requests.get(url).json()
    for base in response ["result"] ["optionList"] :
        is_saved = Deposite_optionlist.objects.filter(Q(dcls_month = base["dcls_month"])&
                                                      Q(fin_co_no = base["fin_co_no"])&
                                                      Q(fin_prdt_cd = base["fin_prdt_cd"])&
                                                      Q(intr_rate_type = base["intr_rate_type"])&
                                                      Q(intr_rate_type_nm = base["intr_rate_type_nm"])&
                                                      Q(save_trm = base["save_trm"])&
                                                      Q(intr_rate = base["intr_rate"])&
                                                      Q(intr_rate2 = base["intr_rate2"]))
        if not is_saved:
            serializer = Deposite_optionlistSerializer(data=base)
            base = Deposite_baselist.objects.get(fin_prdt_cd = base["fin_prdt_cd"])
            if serializer.is_valid():
                serializer.save(base=base)

    while(now_number != max_number):
        now_number += 1
        url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo={now_number}    '
        response = requests.get(url).json()
        
        for base in response ["result"] ["optionList"] :
            is_saved = Deposite_optionlist.objects.filter(Q(dcls_month = base["dcls_month"])&
                                                          Q(fin_co_no = base["fin_co_no"])&
                                                          Q(fin_prdt_cd = base["fin_prdt_cd"])&
                                                          Q(intr_rate_type = base["intr_rate_type"])&
                                                          Q(intr_rate_type_nm = base["intr_rate_type_nm"])&
                                                          Q(save_trm = base["save_trm"])&
                                                          Q(intr_rate = base["intr_rate"])&
                                                          Q(intr_rate2 = base["intr_rate2"]))
            if not is_saved:
                serializer = Deposite_optionlistSerializer(data=base)
                base = Deposite_baselist.objects.get(fin_prdt_cd = base["fin_prdt_cd"])
                if serializer.is_valid():
                    serializer.save(base=base)

    # 적금
    api_key = settings.API_KEY_PRODUCTS
    now_number = 1
    url = f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo={1}'
    response = requests.get(url).json()
    max_number = response['result']['max_page_no']
    for base in response ["result"] ["baseList"] :
        is_saved = Saving_baselist.objects.filter(fin_prdt_cd=base["fin_prdt_cd"])
        if not is_saved:
            serializer = Saving_baselistSerializer(data=base)
            if serializer.is_valid():
                serializer.save()
    
    while(now_number != max_number):
        now_number += 1
        url = f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo={now_number}'
        response = requests.get(url).json()
        for base in response ["result"] ["baseList"] :
            is_saved = Saving_baselist.objects.filter(fin_prdt_cd=base["fin_prdt_cd"])
            if not is_saved:
                serializer = Saving_baselistSerializer(data=base)
                if serializer.is_valid():
                    serializer.save()
    now_number = 1
    url = f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo={1}'
    response = requests.get(url).json()
    
    for base in response ["result"] ["optionList"] :
        is_saved = Saving_optionlist.objects.filter(Q(dcls_month = base["dcls_month"])&
                                                    Q(fin_co_no = base["fin_co_no"])&
                                                    Q(fin_prdt_cd = base["fin_prdt_cd"])&
                                                    Q(intr_rate_type = base["intr_rate_type"])&
                                                    Q(intr_rate_type_nm = base["intr_rate_type_nm"])&
                                                    Q(save_trm = base["save_trm"])&
                                                    Q(intr_rate = base["intr_rate"])&
                                                    Q(intr_rate2 = base["intr_rate2"])&
                                                    Q(rsrv_type = base["rsrv_type"])&
                                                    Q(rsrv_type_nm = base["rsrv_type_nm"]))
        if not is_saved:
            serializer = Saving_optionlistSerializer(data=base)
            base = Saving_baselist.objects.get(fin_prdt_cd = base["fin_prdt_cd"])
            if serializer.is_valid():
                serializer.save(base=base)
    while(now_number != max_number):
        now_number += 1
        url = f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo={now_number}'
        response = requests.get(url).json()
        for base in response ["result"] ["optionList"] :
            is_saved = Saving_optionlist.objects.filter(Q(dcls_month = base["dcls_month"])&
                                                        Q(fin_co_no = base["fin_co_no"])&
                                                        Q(fin_prdt_cd = base["fin_prdt_cd"])&
                                                        Q(intr_rate_type = base["intr_rate_type"])&
                                                        Q(intr_rate_type_nm = base["intr_rate_type_nm"])&
                                                        Q(save_trm = base["save_trm"])&
                                                        Q(intr_rate = base["intr_rate"])&
                                                        Q(intr_rate2 = base["intr_rate2"])&
                                                        Q(rsrv_type = base["rsrv_type"])&
                                                        Q(rsrv_type_nm = base["rsrv_type_nm"]))
            if not is_saved:
                serializer = Saving_optionlistSerializer(data=base)
                base = Saving_baselist.objects.get(fin_prdt_cd = base["fin_prdt_cd"])
                if serializer.is_valid():
                    serializer.save(base=base)

    # 은행
    api_key = settings.API_KEY_PRODUCTS
    now_number = 1
    url = f'http://finlife.fss.or.kr/finlifeapi/companySearch.json?auth={api_key}&topFinGrpNo=020000&pageNo={1}'
    response = requests.get(url).json()
    max_number = response['result']['max_page_no']
    for base in response ["result"] ["baseList"] :
        is_saved = Bank.objects.filter(fin_co_no=base["fin_co_no"])
        if not is_saved:
            serializer = BanklistSerializer(data=base)
            if serializer.is_valid():
                serializer.save()

    while(now_number != max_number):
        now_number += 1
        url = f'http://finlife.fss.or.kr/finlifeapi/companySearch.json?auth={api_key}&topFinGrpNo=020000&pageNo={now_number}    '
        response = requests.get(url).json()
        for base in response ["result"] ["baseList"] :
            is_saved = Bank.objects.filter(fin_co_no=base["fin_co_no"])
            if not is_saved:
                serializer = BanklistSerializer(data=base)
                if serializer.is_valid():
                    serializer.save()

    return Response(status=status.HTTP_200_OK)

    
@api_view(['GET'])
def bank(request):
    banks = Bank.objects.all()
    serializer = BanklistSerializer(banks, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)    


@api_view(['GET'])
def deposite_all(request):
    deposites = Deposite_baselist.objects.all()
    serializer = DepositeListSerializer(deposites, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
        
@api_view(['GET'])
def deposite_detail(request, fin_prdt_cd):
    deposites = Deposite_baselist.objects.filter(fin_prdt_cd=fin_prdt_cd)
    serializer = DepositeListSerializer(deposites, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
        
@api_view(['GET'])
def saving_all(request):
    savings = Saving_baselist.objects.all()
    serializer = SavingListSerializer(savings, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def savinng_detail(request, fin_prdt_cd):
    savings = Saving_baselist.objects.filter(fin_prdt_cd=fin_prdt_cd)
    serializer = SavingListSerializer(savings, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST',])
def userproduct(request):
    user = User.objects.get(username=request.user)
    if request.method == 'POST':
        serializer1 = CustomUserDetailsSerializer(instance=user)
        if serializer1.data["financial_products"]:
            data = (serializer1.data["financial_products"])
            data={'financial_products': data + ',' + request.data['financial_products']+''}
        else:
            data = ''
            data={'financial_products': data + request.data['financial_products']+''}
        print(data)
        
        serializer2 = CustomUserDetailsSerializer(instance=user, data=data, partial=True)
        if serializer2.is_valid(raise_exception=True):
            serializer2.save()
            return Response(serializer2.data, status=status.HTTP_200_OK)
        print('error')
        return Response({'error'})
