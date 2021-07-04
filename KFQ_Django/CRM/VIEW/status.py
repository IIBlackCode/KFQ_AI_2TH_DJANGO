from django.http import HttpResponse
from django.shortcuts import render
import sqlite3
from CRM.models import ClassList, Member, Student_list
from datetime import timedelta, date, time, datetime
from django.utils import timezone
from django.utils.dateformat import DateFormat
from django.utils.dateparse import parse_datetime
from CRM.forms import NoviceForm

#임시

class Status :
    def status(request):
        print("PAGE : status")
        page ='status'
        lst_status = Student_list.objects.all()
        lst_name = []
        lst_date = []
        lst_input_time = []
        lst_output_time = []


        for d in lst_status:
            lst_name.append(d.member_fk)
            #print(d.member_fk.name)
            if d.date and d.output_time:
                d.date = d.date.strftime('%Y-%m-%d')
                d.input_time = d.input_time.strftime('%H:%M:%S')
                d.output_time = d.output_time.strftime('%H:%M:%S')
                d.total_time = Status.diff_time(d.output_time, d.input_time)
                d.absent = Status.check_status(d.input_time, d.output_time)
            elif d.input_time and not d.output_time:
                d.date = d.date.strftime('%Y-%m-%d')
                d.input_time = d.input_time.strftime('%H:%M:%S')
                d.absent = '미퇴실'
            else:
                d.absent = '결석'

            #lst_date.append(d.date.strftime('%Y:%m:%d'))
            #lst_input_time.append(d.input_time.strftime('%H:%M:%S'))
            #lst_output_time.append(d.output_time.strftime('%H:%M:%S'))

            #print(d.date)
            #print(d.input_time)
            #print(d.output_time)
            #print(d.total_time)

        context = {
            'lst_status' : lst_status,
            'lst_date' : lst_date,
            'lst_input_time' : lst_input_time,
            'lst_output_time' : lst_output_time,
        }
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

        print(time_stay)

        if diff_time.days < 0 and time_stay > 5:
            print('late')
            result = '지각'
            return result
        elif time_stay < 7:
            result = '조퇴/외출'
            return result
        else:
            result = '출석'
            print('done')
            return result
        

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


        

#***********************************************************************#    