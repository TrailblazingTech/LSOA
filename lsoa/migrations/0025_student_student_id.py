# Generated by Django 2.0.4 on 2018-09-04 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lsoa', '0024_auto_20180904_0947'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_id',
            field=models.CharField(max_length=30, null=True, unique=True),
        ),
    ]
