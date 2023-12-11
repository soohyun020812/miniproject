from django.db import models

# Create your models here.
# 입력된 값으로 주소를 추리도록 
# 2. 업종선택을 눌렀을 때 쿼리에서 중식 및 한식 이런식으로 선택하도록 

from django import forms
from service.models import MyModel

class MyForm(forms.ModelForm):
    class Meta:  # 클래스 안에 Meta 라는 이름의 클래스 또 생성
        model = MyModel
        fields = ["store_name", "store_code", "store_segment", "address_dong", "address_road", "longitude", "latitude"]

        labels = {
            "store_name": "상호명",
            "store_code": "업종코드",
            "store_segment": "업종분류명",
            "address_dong": "법정동명",
            "address_road": "도로명",
            "longitude": "경도",
            "latitude": "위도",
            "wdate":"wdate"
        }

from service.models import UserInputModel

class UserInputForm(forms.ModelForm):
    class Meta:
        model = UserInputModel
        fields = ["store_location", "store_select", "store_area"]
        labels = {
            "store_location": "점포위치",
            "store_select": "업종선택",
            "store_area": "분석영역"
        }
        
from service.models import Signup


class SignupForm(forms.ModelForm):
    class Meta:
        model = Signup
        fields = ['nickname', 'userid', 'password', 'passwordcheck', 'email', 'phone']
        labels = {
            'nickname': '닉네임',
            'userid': '아이디',
            'password': '패스워드',
            'passwordcheck': '패스워드 확인',
            'email': '이메일',
            'phone': '전화번호'
        }
