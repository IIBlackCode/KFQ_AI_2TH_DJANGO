# Generated by Django 3.2.4 on 2021-07-05 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CRM', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='class_fk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='CRM.classlist'),
        ),
    ]