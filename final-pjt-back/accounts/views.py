from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import CustomUserDetailsSerializer
from .models import User
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from django.core.mail import EmailMessage
import random
# Create your views here.


@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def userinfo(request):
    user = User.objects.get(username=request.user)
    if request.method == 'GET':
        serializer = CustomUserDetailsSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)
    elif request.method == 'PUT':
        print(request.data, request.user)
        serializer = CustomUserDetailsSerializer(instance=user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        print('bad')
        return Response(serializer.error_messages, status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def changepassword(request):
    user = request.user
    new_password1 = request.data.get('new_password1')
    new_password2 = request.data.get('new_password2')
    if new_password1 and new_password1==new_password2:
        user.set_password(new_password1)
        user.save()
        return Response({'msg': '비밀번호 변경완료'})
    else:
        return Response({'msg': '새로운 비밀번호를 확인해주세요'})
    

@api_view(['POST'])
def findpassword(request):
    username = request.data.get('username')
    email = request.data.get('email')
    user = User.objects.filter(Q(username=username) & Q(email=email))
    if user:
        word = list(map( lambda x: str(x),list(range(0, 10)))) + list(map(lambda x: chr(x+ord('a')),range(0, 26)))
        password = ''
        for i in range(20):
            idx = random.randrange(len(word))
            password += word[idx]
        user[0].set_password(password)
        user[0].save()
        email_data = EmailMessage(
            '석세권 뱅크 비밀번호 찾기', #이메일 제목
            f'비밀번호 : {password}', #내용
            to=[f'{user[0].email}'], #받는 이메일
        )
        email_data.send()
        return Response({'msg': 'success'})
    return Response({'msg': 'fail'})


