from django.http import HttpResponse
from django.shortcuts import render
import sqlite3
from CRM.models import ClassList, Member, Student_list
from datetime import timedelta, date, time, datetime
from django.utils import timezone
from django.utils.dateformat import DateFormat
from django.utils.dateparse import parse_datetime

class Status:
   def status(request):
        print("PAGE : status")
        page ='status'
        lst_status = Student_list.objects.all()
        lst_name = []
        lst_date = []
        lst_input_time = []
        lst_output_time = []


        for d in lst_status:
            lst_name.append(d.studentListNum)
            #print(d.studentListNum)
            d.date = d.date.strftime('%Y-%m-%d')
            d.inout_time = d.inout_time.strftime('%H:%M:%S')
            d.output_time = d.output_time.strftime('%H:%M:%S')

            #lst_date.append(d.date.strftime('%Y:%m:%d'))
            #lst_input_time.append(d.inout_time.strftime('%H:%M:%S'))
            #lst_output_time.append(d.output_time.strftime('%H:%M:%S'))

            #print(d.date)
            #print(d.inout_time)
            #print(d.output_time)

        context = {
            'lst_status' : lst_status,
            'lst_date' : lst_date,
            'lst_input_time' : lst_input_time,
            'lst_output_time' : lst_output_time,
        }
        return render(request, './crm/03_status.html', context)
