from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from CRM.forms import UserForm
from django.http import HttpResponseRedirect
from CRM.models import Member


class Account:

    def signup(request):
<<<<<<< HEAD
        if request.method == 'POST':
        # 회원정보 저장
            
            name = request.POST.get('name')
            birth = request.POST.get('birth')
            email = request.POST.get('email')
            pwd = request.POST.get('password')
            Address = request.POST.get('address')
            Univ = request.POST.get('university')
            Major = request.POST.get('major')
            Language = request.POST.get('interest_language')
            user = Member( name=name,birth=birth, email=email, pwd=pwd,
                            Address=Address, Univ=Univ, Major= Major ,Language=Language)
            user.save()
            return HttpResponseRedirect('/index/')
        return render(request, './crm/page/account/signup.html')


    def signin(request):
        if request.method == 'POST':
        # 회원정보 조회
            email = request.POST.get('email')
            pwd = request.POST.get('pwd')

            try:
        # select * from user where email=? and pwd=?
                user = Member.objects.get(email=email, pwd=pwd)
                return render(request, 'signin_success.html')
            except:
                return render(request, 'signin_fail.html')
        return render(request, './crm/page/account/signin.html')

    def signout(request):
        del request.session['email'] # 개별 삭제
        request.session.flush() # 전체 삭제

        return HttpResponseRedirect('/index/')



    # def logout(request):

        
    #     return render(request, './crm/page/account/login.html')
    
    # def login(request):
        
    #     # html 값 받아오기
    #     input_email = request.POST.get('username')
    #     input_password = request.POST.get('password')
    #     print(input_email,input_password)

    #     # if input_password == :
    #     #     print("이메일을 입력하세요.")
    #     # elif input_email == 1:
    #     #     print("비밀번호를 입력하세요.")
    #     # elif input_password and input_email :
    #     #     print("비밀 번호와 이메일을 입력하세요.")
    #     # 로그인 성공한 경우
    #         # index로 이동
    

    #     return render(request, './crm/page/account/login.html')

    # def signup(request):
    #         """
    #         계정생성
    #         """
    #         if request.method == "POST":
    #             form = UserForm(request.POST)
    #             if form.is_valid():
    #                 form.save()
    #                 username = form.cleaned_data.get('username')
    #                 raw_password = form.cleaned_data.get('password1')
    #                 user = authenticate(username=username, password=raw_password)
    #                 login(request, user)
    #                 return redirect('index')
    #         else:
    #             form = UserForm()
    #         return render(request, '../templates/crm/page/account/signup.html', {'form': form})
=======
        """
        계정생성
        """
        if request.method == "POST":
            form = UserForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('index')
        else:
            form = UserForm()
        return render(request, './crm/account/signup.html', {'form': form})

    def addnovice(request):
            if request.method == "POST":
                form = UserForm(request.POST)
                if form.is_valid():
                    form.save()
                    username = form.cleaned_data.get('username')
                    raw_password = form.cleaned_data.get('password1')
                    user = authenticate(username=username, password=raw_password)
                    login(request, user)
                    return redirect('index')
            else:
                form = UserForm()
            return render(request, './crm/account/add_novice.html', {'form': form})
>>>>>>> 4aefb8490ae9c69650d21e76c36842a8eb6680a3
