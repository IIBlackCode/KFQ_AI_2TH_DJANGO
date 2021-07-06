from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
import sqlite3
from CRM.models import ClassList, Member, Student_list
from datetime import timedelta, date, time, datetime
from django.utils import timezone
from django.utils.dateformat import DateFormat
from django.utils.dateparse import parse_datetime
from CRM.forms import NoviceForm, UserForm
from django.contrib import messages

class Status :
    def status(request):
        print("PAGE : status")
        page ='status'
        
        classlist = ClassList.objects.all()
        list_name = []
        list_date = []
        list_input_time = []
        list_output_time = []
        list_class_filter = 0

        if request.method == "POST":
            click_search = request.POST.get('ajax_class_name')
            print('========================')
            print('click_search',click_search)

            for object in classlist:
                if object.class_name == click_search:
                    list_class_filter = object.class_id

        list_status = Student_list.objects.filter(class_fk=list_class_filter)
                    
        for object in list_status:
            print('=========================================')
            print('html 넘겨줘~')
            print('list_class_filter', list_class_filter)
            print(object.member_fk.class_fk_id)

            if list_class_filter  == object.member_fk.class_fk_id:
                list_name.append(object.member_fk)
                # Class casting, 다형성
                # 모든 클래스의 부모는 뭐다? Object클래스
                # 캡슐화, 정보은닉, 추상화, 상속성, 다형성(같은상속관계에서 타입을 변경하는 것을 의미합니다.)
                #print(object.member_fk.name)
                if object.date and object.output_time:
                    object.date = object.date.strftime('%Y-%m-%d')
                    object.input_time = object.input_time.strftime('%H:%M:%S')
                    object.output_time = object.output_time.strftime('%H:%M:%S')
                    object.total_time = Status.diff_time(object.output_time, object.input_time)
                    object.absent = Status.check_status(object.input_time, object.output_time)
                elif object.input_time and not object.output_time:
                    object.date = object.date.strftime('%Y-%m-%d')
                    object.input_time = object.input_time.strftime('%H:%M:%S')
                    object.absent = '미퇴실'
                else:
                    object.absent = '결석'

                context = {
                'list_status' : list_status,
                'list_date' : list_date,
                'list_input_time' : list_input_time,
                'list_output_time' : list_output_time,
                'classlist' : classlist,
                }
            else:
                context = {
                    'classlist' : classlist,
                }

            #lst_date.append(object.date.strftime('%Y:%m:%d'))
            #lst_input_time.append(object.input_time.strftime('%H:%M:%S'))
            #lst_output_time.append(object.output_time.strftime('%H:%M:%S'))

            #print(object.date)
            #print(object.input_time)
            #print(object.output_time)
            #print(object.total_time)

        return render(request, './crm/03_status.html', context)

    def diff_time(time_in,time_out):
        t2 = datetime.strptime(time_out,'%H:%M:%S')
        t1 = datetime.strptime(time_in,'%H:%M:%S')
        time_stay = abs(t2-t1)
        result = time(time_stay.seconds //3600, (time_stay.seconds // 60) % 60).strftime('%H:%M')
        return result

    def check_status(time_in, time_out):
        
        #chk_time = time(diff_time.seconds//3600, (diff_time.seconds//60)%60).strftime('%H:%M')
        #print(chk_time)

        standard_time = datetime.strptime('09:39:59','%H:%M:%S')
        t1 = datetime.strptime(time_in,'%H:%M:%S')
        t2 = datetime.strptime(time_out,'%H:%M:%S')
        
        diff_time = standard_time - t1
        #print(time_in)
        #print(diff_time.days)

        time_stay = t2-t1
        time_stay= time_stay.seconds //3600
        result = ''

        #print(time_stay)

        if diff_time.days < 0 and time_stay > 5:
            #print('late')
            result = '지각'
            return result
        elif time_stay < 7:
            result = '조퇴/외출'
            return result
        else:
            result = '출석'
            #print('done')
            return result
        
    def addnovice(request):
        print("PAGE : add_novice")

        if request.method == "POST":
            
            #form = NoviceForm()
            #newbie = form.save(commit=False)
            newbie_name = request.POST.get('name')
            #print(newbie_name)
            newbie_birth = request.POST.get('birth')
            newbie_email = request.POST.get('email')
            newbie_digits = request.POST.get('digits')
            newbie_address = request.POST.get('address')
            newbie_univ = request.POST.get('univ')
            newbie_major = request.POST.get('major')
            newbie_language = request.POST.get('language')


            newbie = Member.objects.create(email=newbie_email,
                class_fk_id=1,
                name=newbie_name,age = '28',university=newbie_univ,major=newbie_major,
                interest_language=newbie_language, phone_number=newbie_digits, address=newbie_address,
                birth=newbie_birth, seat_num=1, authority='수강생')
            newbie.save()
            
            """
            if form.is_valid():
                newbie = form.save(commit=False)
                novice_name = request.POST.get('name')
                print(novice_name)

                newbie.create(email='zz@cc.cc',
                class_fk_id=newbie.objects.get(class_id=1),
                name=novice_name,age = '28',university='kfq',major='sw',
                interest_language='python',phone_number='000-0000-0000', address='서울시 구로구',
                temperature = 36.5, birth='1994-07-04',seat_num=1,authority='학생')

                return redirect('index')
            else:
                form = NoviceForm()
            """
        return render(request, './crm/page/account/add_novice.html')

    def signup(request):
        print("PAGE : status")
        page ='status'
        classlist = ClassList.objects.all()
        context = {
            'classlist' : classlist,
            'page':page,
        }

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
            elif password is None or password.strip() == ''or email is None or email.strip() == '':
                messages.error(request, '필수 사항을 입력하세요.')
            elif password is None or password.strip() == '':
                messages.error(request, '비밀번호를 입력하세요.')
            elif email is None or email.strip() == '':
                messages.error(request, '이메일을 입력하세요.')
            else:
                user = Member.objects.create( name=name,birth=birth, email=email, password=password,
                                address=address, university=university, major= major ,interest_language=interest_language
                                ,authority=authority,phone_number=phone_number)
                user.save()
                return HttpResponseRedirect('#')
        return redirect('CRM:status')


        

#***********************************************************************#    