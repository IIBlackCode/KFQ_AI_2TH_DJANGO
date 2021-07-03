from django.http import HttpResponse
from django.shortcuts import render
import sqlite3
from CRM.models import ClassList, Member, Student_list
from datetime import timedelta, date, time, datetime
from django.utils import timezone
from django.utils.dateformat import DateFormat
from django.utils.dateparse import parse_datetime

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
            d.date = d.date.strftime('%Y-%m-%d')
            d.inout_time = d.inout_time.strftime('%H:%M:%S')
            d.output_time = d.output_time.strftime('%H:%M:%S')
            d.total_time = Status.diff_time(d.output_time, d.inout_time)
           
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

#***********************************************************************#    