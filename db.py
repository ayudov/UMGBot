from mongoengine import *
from datetime import datetime

connect('ugm_bot')


class Student(Document):
    Fio = StringField(required=True)
    Birth_day = DateTimeField(required=True)
    Dormitory = IntField()


class Lessons(Document):
    Name = StringField(max_length=50, required=True)
    Teacher = StringField(max_length=50, required=True)
    Number = IntField(min_value=1, max_value=10, required=True)


class Group(Document):
    Name = StringField(max_length=10, required=True)
    University = StringField(max_length=50, required=True)
    Year = IntField(min_value=1, max_value=7, required=True)
    Students = ListField(ReferenceField(Student))
    Schedule = ListField(ReferenceField(Lessons))
    Lesson_time = DateTimeField(required=True)


class User(Document):
    user_id = IntField()
    Name = StringField(required=True)
    state = StringField(required=True)
    Reg_time = DateTimeField(required=True)

    # meta = {'allow_inheritance': True}


# Fedor = Student(Fio='Fedor', Birth_day=datetime.utcnow(), Dormitory='3').save()
# Andrey = Student(Fio='Andrey', Birth_day=datetime.utcnow(), Dormitory='3').save()
# Math = Lessons(Name='math', Teacher='Orlovskyy', Number=9).save()
# Group(Name='IK-61', University='KPI', Year=3, Students=[Andrey, Fedor], Schedule=[Math], Lesson_time=datetime.utcnow()).save()

# for post in Student.objects:
#    print(post.Birth_day)
