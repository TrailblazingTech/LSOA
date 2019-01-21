# Generated by Django 2.0.4 on 2018-07-26 20:45

from django.db import migrations, models
import django.db.models.deletion
import django.contrib.postgres.fields



class Migration(migrations.Migration):

    dependencies = [
        ('kidviz', '0015_auto_20180720_2036'),
    ]

    operations = [
        migrations.AddField(
            model_name='observation',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='kidviz.Course'),
        ),
        migrations.AddField(
            model_name='observation',
            name='name',
            field=models.CharField(blank=True, default='', max_length=75),
        ),
        migrations.AddField(
            model_name='observation',
            name='grouping',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    to='kidviz.StudentGrouping'),
        ),
        migrations.AddField(
            model_name='observation',
            name='construct_choices',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=[], null=True, size=None),
        ),
    ]