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
    age = models.IntegerField()
    university = models.CharField(max_length=50,default = '')
    major = models.CharField(max_length=50,default = '')
    interest_language = models.CharField(max_length=50,default = '')
    phone_number = models.CharField(max_length=100,default = '')
    address = models.CharField(max_length=200,default = '')
    temperature = models.FloatField(default = '')
    birth = models.DateField()

class Student_list(models.Model):
    studentListNum = models.AutoField(ClassList, primary_key=True)
    member_fk = models.ForeignKey(Member, on_delete=models.CASCADE)
    date = models.DateTimeField()
    attendance = models.CharField(max_length=2,default='N')
    absent = models.CharField(max_length=2,default='N')
    late = models.CharField(max_length=2,default='N')
    early= models.CharField(max_length=2,default='N')
    inout_time = models.TimeField()
    output_time= models.TimeField()
    total_time = models.TimeField()