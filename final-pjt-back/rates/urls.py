from django.urls import path
from . import views

app_name = 'rates'
urlpatterns = [
    path('', views.exchange_rate, name='exchange_rate'), # 전체 환율 정보 출력시키고 데이터 삽입시킬 생각으로 만듬
    path('update/', views.index, name='index'), # 전체 환율 정보를 받아와서 이미 DB에 있다면 업데이트, 없다면 새로 DB에 생성
]
