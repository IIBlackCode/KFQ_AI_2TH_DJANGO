from django.http import HttpResponse
from django.shortcuts import render
import sqlite3
from CRM.models import ClassList, Member, Student_list
from datetime import timedelta, date, time, datetime
from django.utils import timezone
from django.utils.dateformat import DateFormat
from django.utils.dateparse import parse_datetime

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
                d.inout_time = d.inout_time.strftime('%H:%M:%S')
                d.output_time = d.output_time.strftime('%H:%M:%S')
                d.total_time = Status.diff_time(d.output_time, d.inout_time)
                d.absent = Status.check_status(d.inout_time, d.output_time)
            elif d.inout_time and not d.output_time:
                d.date = d.date.strftime('%Y-%m-%d')
                d.inout_time = d.inout_time.strftime('%H:%M:%S')
                d.absent = '미퇴실'
            else:
                d.absent = '결석'

            #lst_date.append(d.date.strftime('%Y:%m:%d'))
            #lst_input_time.append(d.inout_time.strftime('%H:%M:%S'))
            #lst_output_time.append(d.output_time.strftime('%H:%M:%S'))

            #print(d.date)
            #print(d.inout_time)
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
        


        

#***********************************************************************#    