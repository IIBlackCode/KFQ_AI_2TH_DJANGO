from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
import sqlite3
from CRM.models import ClassList, Member, Student_list
from datetime import timedelta, date, time, datetime
from django.utils import timezone
from django.utils.dateformat import DateFormat
from django.utils.dateparse import parse_datetime
#***********************************************************************#    

class SeatingChart:
    def test(request):
        print("PAGE : test")
        test = Member.objects.all()
        page ='SeatingChart'
        test_test=[]
        for n in test:
            test_test.append(n.class_fk)
        context = {
            'test':test, 'test_test':test_test, 'page' : page
        }
        return render(request, './crm/05_seatingChart.html', context)