# Generated by Django 3.2.4 on 2021-07-04 16:18

import CRM.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassList',
            fields=[
                ('class_id', models.AutoField(primary_key=True, serialize=False)),
                ('class_name', models.CharField(max_length=50)),
                ('student_count', models.IntegerField()),
                ('open_date', models.DateTimeField()),
                ('close_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('email', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField(null=True)),
                ('university', models.CharField(default='', max_length=50, null=True)),
                ('major', models.CharField(default='', max_length=50, null=True)),
                ('interest_language', models.CharField(default='', max_length=50, null=True)),
                ('phone_number', models.CharField(default='', max_length=100, null=True)),
                ('address', models.CharField(default='', max_length=200, null=True)),
                ('birth', models.DateField(null=True)),
                ('seat_num', models.IntegerField(null=True)),
                ('authority', models.CharField(max_length=50)),
                ('class_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CRM.classlist')),
            ],
        ),
        migrations.CreateModel(
            name='Student_list',
            fields=[
                ('studentListNum', models.AutoField(primary_key=True, serialize=False, verbose_name=CRM.models.ClassList)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('attendance', models.CharField(default='N', max_length=2, null=True)),
                ('absent', models.CharField(default='N', max_length=2, null=True)),
                ('late', models.CharField(default='N', max_length=2, null=True)),
                ('early', models.CharField(default='N', max_length=2, null=True)),
                ('input_time', models.DateTimeField(null=True)),
                ('output_time', models.DateTimeField(null=True)),
                ('total_time_outing', models.DateTimeField(null=True)),
                ('total_time', models.DateTimeField(null=True)),
                ('temperature', models.FloatField(null=True)),
                ('member_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CRM.member')),
            ],
        ),
    ]
