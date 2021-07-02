from django.http import HttpResponse ,JsonResponse
from django.shortcuts import render
import sqlite3
#***********************************************************************#
# Dashboard 통계
conn = sqlite3.connect("db.sqlite3",check_same_thread=False)
cur = conn.cursor()

class Dashboard :
    #총 출석 수
    def total_attendance(request):
        conn = sqlite3.connect("db.sqlite3",check_same_thread=False)
        cur = conn.cursor()
        cur.execute("select count(*) from CRM_student_list WHERE attendance like 'Y' ")
        count = cur.fetchone()
        print('출석 수 : ',count[0])
            
        return JsonResponse({'count' :count[0]},status=200)

    #총 결석 수
    def total_absent(request):
        conn = sqlite3.connect("db.sqlite3",check_same_thread=False)
        cur = conn.cursor()
        cur.execute("select count(*) from CRM_student_list WHERE absent like 'Y' ")
        count = cur.fetchone()
        print('결석 수 : ',count[0])
            
        return JsonResponse({'count' :count[0]},status=200)

    #총 지각 수
    def total_late(request):
        conn = sqlite3.connect("db.sqlite3",check_same_thread=False)
        cur = conn.cursor()
        cur.execute("select count(*) from CRM_student_list WHERE late like 'Y' ")
        count = cur.fetchone()
        print('지각 수 : ',count[0])
            
        return JsonResponse({'count' :count[0]},status=200)

    #총 조퇴 수
    def total_early(request):
        conn = sqlite3.connect("db.sqlite3",check_same_thread=False)
        cur = conn.cursor()
        cur.execute("select count(*) from CRM_student_list WHERE early like 'Y' ")
        count = cur.fetchone()
        print('조퇴 수 : ',count[0])
            
        return JsonResponse({'count' :count[0]},status=200)


    def class_statistics(request):
        class_fk = request.GET.get('class_fk')
        print('class_fk :',str(class_fk))
        conn = sqlite3.connect("db.sqlite3",check_same_thread=False)
        cur = conn.cursor()
        with conn:
            cur.execute("select count(*) from CRM_student_list t1, CRM_member t2 WHERE t1.member_fk_id = t2.email AND t1.attendance like 'Y' AND t2.class_fk_id ="+class_fk)
            attendance = cur.fetchone()
            print('반 출석 수 : ',attendance[0])
        with conn:
            cur.execute("select count(*) from CRM_student_list t1, CRM_member t2 WHERE t1.member_fk_id = t2.email AND t1.absent like 'Y' AND t2.class_fk_id ="+class_fk)
            absent = cur.fetchone()
            print('반 결석 수 : ',absent[0])
        with conn:
            cur.execute("select count(*) from CRM_student_list t1, CRM_member t2 WHERE t1.member_fk_id = t2.email AND t1.late like 'Y' AND t2.class_fk_id ="+class_fk)
            late = cur.fetchone()
            print('반 지각 수 : ',late[0])
        with conn:
            cur.execute("select count(*) from CRM_student_list t1, CRM_member t2 WHERE t1.member_fk_id = t2.email AND t1.early like 'Y' AND t2.class_fk_id ="+class_fk)
            early = cur.fetchone()
            print('반 조퇴 수 : ',early[0])

        context = {
            'attendance':attendance,
            'absent':absent,
            'late':late,
            'early':early,
        }
        return JsonResponse({'context' :context},status=200)
    