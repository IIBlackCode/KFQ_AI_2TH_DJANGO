# Generated by Django 3.2.4 on 2021-07-03 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRM', '0003_auto_20210703_0244'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='class_fk',
            new_name='class_fk_id',
        ),
        migrations.AlterField(
            model_name='student_list',
            name='inout_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='student_list',
            name='output_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='student_list',
            name='total_time',
            field=models.DateTimeField(null=True),
        ),
    ]
