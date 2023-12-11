from django import forms
#모델클래스를 import 해야 한다.
#from 폴더명, 파일명 import 클래스명
from login.models import Member

class MemberForm(forms.ModelForm):
    class Meta:
        model= Member #model 변수에 모델 클래스를 연결한다. 
        fields = ['userid','username','password','email','phone']
        labels={'userid':'아이디',
                'username': '이름',
                'password':'패스워드',
                'email': '이메일',
                'phone': '전화번호'
                }
        
        def clean(self):
        # 빈 메서드로 오버라이드하여 아무 동작도 수행하지 않도록 함
            pass