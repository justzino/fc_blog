from django import forms 

from .models import User

class RegisterForm(forms.ModelForm):
    # 회원가입 폼
    # 장고에서는 HTML 입력요소를 widget(위젯)이라고 말한다. 
    password = forms.CharField(label='password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='confirm password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'gender', 'email']

    def clean_confirm_password(self):       #clean메써드가 호출된후에 호출되는 메써드 clean_필드네임(유효성 검사) ex)clean_username 
        cd = self.cleaned_data
        if cd['password'] != cd['confirm_password']:
            raise forms.ValidationError('비밀번호가 일치하지 않습니다!')

        return cd['confirm_password']


# class LoginForm(forms.ModelForm):
#     # 로그인 폼
#      password = forms.CharField(label='password', widget=forms.PasswordInput)

#      class Meta:
#         model = User
#         fields = ['email', 'password']