# Generated by Django 3.2.4 on 2021-07-03 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CRM', '0007_auto_20210704_0240'),
    ]

    operations = [
        migrations.AddField(
            model_name='seatingchart',
            name='class_list_fk',
            field=models.ForeignKey(db_column='class_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='CRM.classlist'),
        ),
    ]
