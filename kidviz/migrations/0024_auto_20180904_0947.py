# Generated by Django 2.0.4 on 2018-09-04 09:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('kidviz', '0023_auto_20180904_0936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contexttag',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    related_name='kidviz_contexttag_owner', to=settings.AUTH_USER_MODEL,
                                    verbose_name='owner'),
        ),
    ]
