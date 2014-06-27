from django.test import TestCase
from django.utils import unittest
from django.test import Client
from django.test.client import RequestFactory
from appTraining.models import Group,Lecturer,Student
from appTraining.views import Load
# Create your tests here.
class GroupTestCase(TestCase):
    def setUp(self):
        Group.objects.create(groupNum = "group5")
    def test_group(self):
        group = Group.objects.get(groupNum = "group5")

class LecturerTestCase(TestCase):
    def setUp(self):
        Lecturer.objects.create(name = "Surik", surname = "Eqsuzyan", phoneNum = "058 897-564")
    def test_lecturer(self):
        lect = Lecturer.objects.get(name = "Surik", surname = "Eqsuzyan", phoneNum = "058 897-564")

class StudentTestCase(TestCase):
    def setUp(self):
        Student.objects.create(name = "Aram", surname = "Hovsepyan",groupId=Group(id=1), phoneNum = "058 897-564" )
    def testStudent(self):
        stud = Student.objects.get(name = "Aram", surname = "Hovsepyan", groupId=Group(id=1), phoneNum = "058 897-564")
        
class LoadTest(unittest.TestCase):
    def setUp(self):
        self.factory = RequestFactory()
    def test_load(self):
        c = Client()
        response = c.post('/training',{'groupNum': 'group1'})
        self.assertEqual(response.status_code, 200)
        response = c.get('/training')
        response.content
    #    request = self.factory.get('/training')
     #   response = Load(request)
 #       self.assertEqual(response.status_code, 200)
