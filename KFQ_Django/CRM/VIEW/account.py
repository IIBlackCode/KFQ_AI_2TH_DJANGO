from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from CRM.forms import UserForm, NoviceForm

class Account:

    def signup(request):
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
        print("PAGE : add_novice")
        if request.method == "POST":
            form = NoviceForm()
            if form.is_valid():
                newbie = form.save(commit=False)
                novice_name = newbie.name
                print(novice_name)

                newbie.objects.create(email='zz@cc.cc',
                class_fk_id=newbie.objects.get(class_id=1),
                name=novice_name,age = '28',university='kfq',major='sw',
                interest_language='python',phone_number='000-0000-0000', address='서울시 구로구',
                temperature = 36.5, birth='1994-07-04',seat_num=1,authority='학생')

                return redirect('index')
        else:
            form = NoviceForm()
        return render(request, './crm/page/account/add_novice.html', {'form': form})