# Generated by Django 2.0.8 on 2019-03-02 16:09
from django.core.management.sql import emit_post_migrate_signal
from django.db import migrations


def create_groups_and_permissions(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    teachers, _ = Group.objects.get_or_create(name='Teachers')
    administrators, _ = Group.objects.get_or_create(name='Administrators')
    researchers, _ = Group.objects.get_or_create(name='Researchers')

    Course = apps.get_model('kidviz', 'Course')
    Student = apps.get_model('kidviz', 'Student')
    StudentGroup = apps.get_model('kidviz', 'StudentGroup')
    StudentGrouping = apps.get_model('kidviz', 'StudentGrouping')
    Observation = apps.get_model('kidviz', 'Observation')
    LearningConstruct = apps.get_model('kidviz', 'LearningConstruct')

    Permission = apps.get_model('auth', 'Permission')
    ContentType = apps.get_model('contenttypes', 'ContentType')

    emit_post_migrate_signal(2, False, 'default')  # this creates any missing permissions

    observation_content_type = ContentType.objects.get_for_model(Observation)
    perm_view_nonconsent_observation, _ = Permission.objects.get_or_create(
        codename='can_view_nonconsent_observations',
        name='Can View Observations of Students Without Research Consent',
        content_type=observation_content_type,
    )

    teachers.permissions.add(perm_view_nonconsent_observation)
    administrators.permissions.add(perm_view_nonconsent_observation)
    # researchers are not allowed to see observations for non-consenting students

    # I feel like this should be in a migration... I might have made this manually in the DB
    teachers.permissions.add(Permission.objects.get(codename='add_contexttag'))
    teachers.permissions.add(Permission.objects.get(codename='change_contexttag'))
    teachers.permissions.add(Permission.objects.get(codename='delete_contexttag'))
    administrators.permissions.add(Permission.objects.get(codename='add_contexttag'))
    administrators.permissions.add(Permission.objects.get(codename='change_contexttag'))
    administrators.permissions.add(Permission.objects.get(codename='delete_contexttag'))


class Migration(migrations.Migration):
    dependencies = [
        ('kidviz', '0029_auto_20190302_1608'),
    ]

    operations = [
        migrations.RunPython(create_groups_and_permissions)
    ]
