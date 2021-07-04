# Generated by Django 3.2.4 on 2021-07-03 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CRM', '0006_seatingchart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seatingchart',
            name='member_fk',
            field=models.ForeignKey(db_column='email', on_delete=django.db.models.deletion.CASCADE, to='CRM.member'),
        ),
        migrations.AlterField(
            model_name='seatingchart',
            name='studentlist_fk',
            field=models.ForeignKey(db_column='studentListNum', on_delete=django.db.models.deletion.CASCADE, to='CRM.student_list'),
        ),
    ]