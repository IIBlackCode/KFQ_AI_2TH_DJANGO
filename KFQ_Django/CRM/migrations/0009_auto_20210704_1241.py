# Generated by Django 3.2.4 on 2021-07-04 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRM', '0008_seatingchart_class_list_fk'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='seat_num',
            field=models.IntegerField(null=True),
        ),
        migrations.DeleteModel(
            name='SeatingChart',
        ),
    ]
