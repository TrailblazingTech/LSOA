# Generated by Django 2.0.4 on 2018-04-09 22:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lsoa', '0009_auto_20180409_1239'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContextTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('text', models.CharField(max_length=255)),
                ('last_used', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='lsoa_contexttag_owner', to=settings.AUTH_USER_MODEL, verbose_name='owner')),
            ],
            options={
                'ordering': ['-last_used'],
            },
        ),
    ]
