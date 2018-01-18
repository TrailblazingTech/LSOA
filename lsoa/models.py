from django.db import models
from django_extensions.db.models import TimeStampedModel

from utils.ownership import OwnerMixin


class Course(TimeStampedModel, OwnerMixin):
    name = models.CharField(max_length=255)
    students = models.ManyToManyField('lsoa.Student', blank=True)

    def __str__(self):
        return self.name


class Student(TimeStampedModel):
    '''
    A Student has associated data, however on the Student record itself, simply
    record their name.
    '''
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    nickname = models.CharField(max_length=255, blank=True, default='')

    def __str__(self):
        return '{} {} '.format(self.nickname, self.last_name[0]) if self.nickname else \
            '{} {}'.format(self.first_name, self.last_name[0])


class StudentGroup(TimeStampedModel):
    '''
    A StudentGroup is a container model for students of a course in a group. A
    student can be in multiple groups at the same time but only one group for a
    particular StudentGrouping.
    '''
    name = models.CharField(max_length=255, blank=True, default='')  # optional
    course = models.ForeignKey('lsoa.Course')
    students = models.ManyToManyField('lsoa.Student', blank=True)

    def __str__(self):
        return self.name if self.name else ', '.join(str(student) for student in self.students.all())


class StudentGrouping(TimeStampedModel):
    '''
    A StudentGrouping is a collection of student groups. This is convenient because
    a teacher might say "get in your big groups" where students are in groups of 4-5
    versus "pair up with your study buddy" to put students in pairs.
    '''
    name = models.CharField(max_length=255)
    course = models.ForeignKey('lsoa.Course')
    groups = models.ManyToManyField('lsoa.StudentGroup', blank=True)

    def __str__(self):
        return '{} [{}]'.format(self.name, self.course)


class Observation(TimeStampedModel, OwnerMixin):
    '''
    An Observation is a "snapshot in time" of student(s) exhibiting mastery of
    a certain (or multiple) learning constructs, paired with typed notes or
    visual evidence (picture or video).
    '''
    students = models.ManyToManyField('lsoa.Student', blank=True)  # 0 to n
    student_groups = models.ManyToManyField('lsoa.StudentGroup', blank=True)  # 0 to n
    media = models.FileField(blank=True, null=True)  # optional
    constructs = models.ManyToManyField('lsoa.LearningConstruct', blank=True)  # 0 to n
    notes = models.TextField(blank=True)  # optional

    def __str__(self):
        return 'Observation at {}'.format(self.created)


class LearningConstruct(TimeStampedModel):
    '''
    A LearningConstruct is a ...
    '''
    name = models.CharField(max_length=255)
    abbreviation = models.CharField(max_length=255)

    def __str__(self):
        return '{} ({})'.format(self.name, self.abbreviation)


class LearningConstructLevel(TimeStampedModel):
    '''
    Some description here...
    '''
    construct = models.ForeignKey('lsoa.LearningConstruct')
    level = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return '{} {}'.format(self.construct.abbreviation, self.level)

class LearningConstructSublevel(TimeStampedModel):
    '''
    Some description here...
    '''
    level = models.ForeignKey('lsoa.LearningConstructLevel')
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return '{}'.format(self.name)

class LearningConstructSublevelExample(TimeStampedModel):
    '''
    Some description here...
    '''
    sublevel = models.ForeignKey('lsoa.LearningConstructSublevel', related_name='examples')
    text = models.TextField()

    def __str__(self):
        return '({}) {}'.format(self.sublevel.name, self.text[:50])