import requests
from django.conf import settings
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import ExchangeRate
from .serializers import ExchangeRateSerializer
from datetime import datetime, timedelta

@api_view(['GET'])
def index(request):
    api_key = settings.API_KEY
    today = datetime.today()
    response_list = None
    td = 0
    
    while(not response_list):
        day = today - timedelta(td)
        str_day = day.strftime("%Y%m%d")
        url = f'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={api_key}&searchdate={str_day}&data=AP01'
        response_list= requests.get(url).json()
        td += 1
        
    for li in response_list:
        save_data = {
            'RESULT' : li.get('result'),
            'CUR_UNIT' : li.get('cur_unit'),
            'CUR_NM' : li.get('cur_nm'),
            'TTB' : li.get('ttb'),
            'TTS' : li.get('tts'),
            'DEAL_BAS_R' : li.get('deal_bas_r'),
            'BKPR' : li.get('bkpr'),
            'YY_EFEE_R' : li.get('yy_efee_r'),
            'TEN_DD_EFEE_R' : li.get('ten_dd_efee_r'),
            'KFTC_DEAL_BAS_R' : li.get('kftc_deal_bas_r'),
            'KFTC_BKPR' : li.get('kftc_bkpr'),
        }
        prev_data = ExchangeRate.objects.filter(CUR_UNIT=save_data['CUR_UNIT'])
        if not prev_data:
            serializer = ExchangeRateSerializer(data=save_data)
        else:
            prev_data = ExchangeRate.objects.get(CUR_UNIT=save_data['CUR_UNIT'])
            serializer = ExchangeRateSerializer(instance=prev_data, data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
    return JsonResponse({'message':'saved'})


@api_view(['POST',])
def exchange_rate(request):
    if request.method == 'POST':
        print(request.data)
        depositproducts = ExchangeRate.objects.get(CUR_UNIT=request.data['cur_unit'])
        serializer = ExchangeRateSerializer(depositproducts)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
