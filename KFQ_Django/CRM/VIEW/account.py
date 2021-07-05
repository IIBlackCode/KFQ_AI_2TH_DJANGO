from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from CRM.models import Member
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.hashers import check_password

class Account:

    def signup(request):
        if request.method == 'POST':
        # 회원정보 저장
            name = request.POST.get('name')
            birth = request.POST.get('birth')
            email = request.POST.get('email')
            password = request.POST.get('password')
            repassword = request.POST.get('repassword')
            address = request.POST.get('address')
            university = request.POST.get('university')
            major = request.POST.get('major')
            interest_language = request.POST.get('interest_language')
            authority = request.POST.get('authority')
            phone_number = request.POST.get('phone_number')
            if password != repassword:
                messages.error(request, '비밀번호가 일치 하지 않습니다.')
                return HttpResponseRedirect('/CRM/signup/')
            elif password is None or password.strip() == ''or email is None or email.strip() == '':
                messages.error(request, '필수 사항을 입력하세요.')
                return HttpResponseRedirect('/CRM/signup/')
            elif password is None or password.strip() == '':
                messages.error(request, '비밀번호를 입력하세요.')
                return HttpResponseRedirect('/CRM/signup/')
            elif email is None or email.strip() == '':
                messages.error(request, '이메일을 입력하세요.')
                return HttpResponseRedirect('/CRM/signup/')
            else:
                user = Member.objects.create( name=name,birth=birth, email=email, password=password,
                                address=address, university=university, major= major ,interest_language=interest_language
                                ,authority=authority,phone_number=phone_number)
                user.save()
                return HttpResponseRedirect('/CRM/signin/')
        return render(request, './crm/page/account/signup.html')


    def signin(request):
        if request.method == 'POST':
        # 회원정보 조회
            email = request.POST.get('email')
            password = request.POST.get('password')
            try:
                user = Member.objects.get(email=email, password=password)
                request.session['name'] = user.name
                # request.session['birth'] = user.birth
                request.session['email'] = user.email
                request.session['address'] = user.address
                request.session['university'] = user.university
                request.session['major'] = user.major
                request.session['interest_language'] = user.interest_language
                request.session['authority'] = user.authority
                request.session['phone_number'] = user.phone_number
                return render(request, './crm/page/account/signin_success.html')
            except:
                return render(request, './crm/page/account/signin_fail.html')
        return render(request, './crm/page/account/signin.html')

    def signout(request):
        del request.session['email'] # 개별 삭제
        request.session.flush() # 전체 삭제

        return HttpResponseRedirect('/CRM/signin/')


    def change_pw(request):
        context= {}
        if request.method == "POST":
            current_password = request.POST.get("password")
            user = request.user
            if check_password(current_password,user.password):
                new_password = request.POST.get("password1")
                password_confirm = request.POST.get("password2")
                if new_password == password_confirm:
                    user.set_password(new_password)
                    user.save()
                    Account.signin(request,user)
                    return redirect("CRM:index")
                else:
                    context.update({'error':"새로운 비밀번호를 다시 확인해주세요."})
        else:
            context.update({'error':"현재 비밀번호가 일치하지 않습니다."})

        return render(request, "account/settings.html",context)