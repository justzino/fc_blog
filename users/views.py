from django.shortcuts import render

from .forms import RegisterForm, LoginForm

def register(request):
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)     #commit=False해서 Db에 저장되는 것이 아니라 object가 만들어지는것
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            return render(request, 'registration/login.html', {'user':user})

    else:
        user_form = RegisterForm()

    return render(request, 'registration/register.html', {'user_form':user_form})


def login(request):
    return render(request, 'registration/login.html')