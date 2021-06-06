from django.test import TestCase
from course import serializers
from course.models import Course, Category

class CourseSerializerTest(TestCase):
    def setUp(self):
        category = Category.objects.create(name = "Testcategory", imgpath = "Testimage")

    def test_serializer_create(self):
        serializer_data = {
            "name": "Testname",
            "description": "Testdescription",
            "logo": "Testlogo",
            "category": 1,
            "contacts": [
                    {
                        "contact_type": 1,
                        "value": "Testvalue"
                    }
                ],
            "branches": [
                    {
                        "latitude": "Testlatitude",
                        "longitude": "Testlongitude",
                        "address": "Testaddress"
                    }
                ]
            }			

        serializer = serializers.CourseSerializer(data=serializer_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        self.assertIsNotNone(Course.objects.get(id=1))
