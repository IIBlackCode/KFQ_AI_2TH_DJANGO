# Generated by Django 3.2.4 on 2021-07-02 10:23

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
                ('age', models.IntegerField()),
                ('university', models.CharField(default='', max_length=50)),
                ('major', models.CharField(default='', max_length=50)),
                ('interest_language', models.CharField(default='', max_length=50)),
                ('phone_number', models.CharField(default='', max_length=100)),
                ('address', models.CharField(default='', max_length=200)),
                ('temperature', models.FloatField(default='')),
                ('birth', models.DateField()),
                ('class_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CRM.classlist')),
            ],
        ),
        migrations.CreateModel(
            name='Student_list',
            fields=[
                ('studentListNum', models.AutoField(primary_key=True, serialize=False, verbose_name=CRM.models.ClassList)),
                ('date', models.DateTimeField()),
                ('attendance', models.CharField(default='N', max_length=2)),
                ('absent', models.CharField(default='N', max_length=2)),
                ('late', models.CharField(default='N', max_length=2)),
                ('early', models.CharField(default='N', max_length=2)),
                ('inout_time', models.TimeField()),
                ('output_time', models.TimeField()),
                ('total_time', models.TimeField()),
                ('member_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CRM.member')),
            ],
        ),
    ]