from django.db import models

# Create your models here.

class Deposite_baselist(models.Model): # 예금 기본정보목록
    dcls_end_day = models.TextField(blank=True, null=True) # 공시종료일
    dcls_month = models.TextField() # 공시 제출월 [YYYYMM]
    dcls_strt_day = models.TextField() # 공시 시작일
    etc_note = models.TextField() # 기타 유의사항
    fin_co_no = models.TextField() # 금융회사 코드
    fin_co_subm_day = models.TextField() # 금융회사 제출일 [YYYYMMDDHH24MI]
    fin_prdt_cd = models.TextField() # 금융상품코드
    fin_prdt_nm = models.TextField() # 금융 상품명
    join_deny = models.TextField() # 가입제한 Ex) 1:제한없음, 2:서민전용, 3:일부제한
    join_member = models.TextField() # 가입대상
    join_way = models.TextField() # 가입방법
    kor_co_nm = models.TextField() # 금융회사 명
    max_limit = models.IntegerField(blank=True, null=True) # 최고한도
    mtrt_int = models.TextField() # 만기 후 이자율
    spcl_cnd = models.TextField() # 우대조건
    

class Deposite_optionlist(models.Model): # 예금 옵션목록
    dcls_month = models.TextField() # 공시 제출월 [YYYYMM]
    fin_co_no = models.TextField() # 금융회사 코드
    fin_prdt_cd = models.TextField() # 금융상품코드
    intr_rate = models.FloatField(blank=True, null=True) # 저축 금리 [소수점 2자리]
    intr_rate2 = models.FloatField() # 최고 우대금리 [소수점 2자리]
    intr_rate_type = models.TextField() # 저축 금리 유형
    intr_rate_type_nm = models.TextField() # 저축 금리 유형명
    save_trm = models.TextField()  # 저축 기간 [단위: 개월]
    base = models.ForeignKey(Deposite_baselist, on_delete=models.CASCADE)

class Saving_baselist(models.Model): # 적금
    dcls_end_day = models.TextField(blank=True, null=True) # 공시 종료일
    dcls_month = models.TextField() # 공시 제출월 [YYYYMM]
    dcls_strt_day = models.TextField() # 공시 시작일
    etc_note = models.TextField() # 기타 유의사항
    fin_co_no = models.TextField() # 금융회사 코드
    fin_co_subm_day = models.TextField() # 금융회사 제출일 [YYYYMMDDHH24MI]
    fin_prdt_cd = models.TextField() # 금융상품코드
    fin_prdt_nm = models.TextField() # 금융 상품명
    join_deny = models.TextField() # 가입제한 Ex) 1:제한없음, 2:서민전용, 3:일부제한
    join_member = models.TextField() # 가입대상
    join_way = models.TextField() # 가입방법
    kor_co_nm = models.TextField() # 금융회사 명
    max_limit = models.IntegerField(blank=True, null=True) # 최고한도
    mtrt_int = models.TextField() # 만기 후 이자율
    spcl_cnd = models.TextField() # 우대조건

class Saving_optionlist(models.Model):
    dcls_month = models.TextField() # 공시 제출월 [YYYYMM]
    fin_co_no = models.TextField() # 금융회사 코드
    fin_prdt_cd = models.TextField() # 금융상품코드
    intr_rate = models.FloatField(blank=True, null=True) # 저축 금리 [소수점 2자리]
    intr_rate2 = models.FloatField() # 최고 우대금리 [소수점 2자리]
    intr_rate_type = models.TextField() # 저축 금리 유형
    intr_rate_type_nm = models.TextField() # 저축 금리 유형명
    rsrv_type = models.TextField() # 적립 유형
    rsrv_type_nm = models.TextField() # 적립 유형명
    save_trm = models.TextField()  # 저축 기간 [단위: 개월]
    base = models.ForeignKey(Saving_baselist, on_delete=models.CASCADE)

class Bank(models.Model):
    dcls_month = models.TextField()
    fin_co_no = models.TextField()
    kor_co_nm = models.TextField()
    dcls_chrg_man = models.TextField()
    homp_url = models.TextField()
    cal_tel = models.TextField()