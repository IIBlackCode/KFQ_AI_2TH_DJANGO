from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class ClassList(models.Model):
    class_id = models.AutoField(primary_key=True)
    class_name = models.CharField(max_length=50)
    student_count = models.IntegerField()
    open_date = models.DateTimeField()
    close_date = models.DateTimeField()

    def __str__(self):
        return self.class_name

'''
INSERT INTO CRM_classlist (class_name, student_count, open_date, close_date)
VALUES('AI인공지능',25,'2021-04-26','2021-10-30')
'''

class Member (models.Model):
    #PK
    email = models.CharField(max_length=200, primary_key=True)
    #FK
    class_fk = models.ForeignKey(ClassList, on_delete=models.CASCADE)

    password = models.CharField(max_length=200)
    name = models.CharField(max_length=50)
    age = models.IntegerField(null=True)
    university = models.CharField(max_length=50,default = '',null=True)
    major = models.CharField(max_length=50,default = '',null=True)
    interest_language = models.CharField(max_length=50,default = '',null=True)
    phone_number = models.CharField(max_length=100,default = '',null=True)
    address = models.CharField(max_length=200,default = '',null=True)
    temperature = models.FloatField(default = '',null=True)
    birth = models.DateField(null=True)

class Student_list(models.Model):
    studentListNum = models.AutoField(ClassList, primary_key=True)
    member_fk = models.ForeignKey(Member, on_delete=models.CASCADE)
    #class_fg = models.ForeignKey(ClassList, on_delete=models.CASCADE)

    date = models.DateTimeField(auto_now_add=True)

    #출석, 결석, 지각, 조퇴
    attendance = models.CharField(max_length=2,default='N',null=True)
    absent = models.CharField(max_length=2,default='N',null=True)
    late = models.CharField(max_length=2,default='N',null=True)
    early= models.CharField(max_length=2,default='N',null=True)
    
    inout_time = models.DateTimeField(auto_now_add=True)
    output_time= models.DateTimeField(auto_now_add=True)
    total_time = models.DateTimeField(null=True)