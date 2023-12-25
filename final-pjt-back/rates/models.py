from django.db import models


class ExchangeRate(models.Model):
    SUCCESS = 1
    DATA_ERROR = 2
    AUTH_ERROR = 3
    DAILY_LIMIT = 4

    RESULT_CHOICES = (
        (SUCCESS, '성공'),
        (DATA_ERROR, 'DATA코드 오류'),
        (AUTH_ERROR, '인증코드 오류'),
        (DAILY_LIMIT, '일일제한횟수 마감'),
    )

    RESULT = models.IntegerField(choices=RESULT_CHOICES)  # 조회 결과
    CUR_UNIT = models.CharField(max_length=255)  # 통화코드
    CUR_NM = models.CharField(max_length=255)  # 국가/통화명
    TTB = models.CharField(max_length=255)  # 전신환(송금) 받을때
    TTS = models.CharField(max_length=255)  # 전신환(송금) 보낼때
    DEAL_BAS_R = models.CharField(max_length=255)  # 매매 기준율
    BKPR = models.CharField(max_length=255)  # 장부가격
    YY_EFEE_R = models.CharField(max_length=255)  # 년환가료율
    TEN_DD_EFEE_R = models.CharField(max_length=255)  # 10일환가료율
    KFTC_DEAL_BAS_R = models.CharField(max_length=255)  # 서울외국환중개 매매기준율
    KFTC_BKPR = models.CharField(max_length=255)  # 서울외국환중개 장부가격

    # def __str__(self):
    #     return f"{self.CUR_NM} - {self.CUR_UNIT}"
