from django.test import TestCase
import unittest
from django.test import Client
from appTraining.models import Group,Lecturer,Student
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

class SimpleTest(unittest.TestCase):
    def test_details(self):
        client = Client()
        response = client.get('/training/lecturer')
        self.assertEqual(response.status_code, 200)

    def test_index(self):
        client = Client()
        response = client.get('/customer/index/')
        self.assertEqual(response.status_code, 200)
