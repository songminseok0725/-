from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('', views.index, name='index'),
    path('bank/', views.bank),
    path('deposite/', views.deposite_all, name='deposite_all'),
    path('deposite/<str:fin_prdt_cd>/', views.deposite_detail),
    path('saving/', views.saving_all),
    path('saving/<str:fin_prdt_cd>/', views.savinng_detail),
    path('userproduct/', views.userproduct),
]
