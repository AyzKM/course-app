from rest_framework import status
from django.test import TestCase
from django.urls import reverse
from course.models import Course, Category
from course.serializers import CourseSerializer
import json

class CourseViewsTestCase(TestCase):
    def setUp(self):
        self.url = reverse('courses')

    def test_courselist_loads_success(self):
        response = self.client.get(self.url)
        course_list = Course.objects.all()
        serializer = CourseSerializer(course_list, many=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)

    def test_get_detail_view_success(self):
        category = Category.objects.create(name="Test category", imgpath="Test image")
        course = Course.objects.create(name="Test name", description="Test description", logo="Test logo", category=category)
        response = self.client.get(reverse('course-detail', kwargs={'pk': course.pk}))
        course = Course.objects.get(pk=course.pk)
        serializer = CourseSerializer(course)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)

    def test_delete_view_success(self):
        category = Category.objects.create(name = "Testcategory", imgpath = "Testimage")
        course = Course.objects.create(name="Testname", description="Testdescription", logo="Testlogo", category=category)
        response = self.client.delete(reverse('course-delete', kwargs={'pk': course.pk}))
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_get_detail_view_invalid(self):
        response = self.client.get(reverse('course-detail', kwargs={'pk': 23}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_view_success(self):
        Category.objects.create(name="Test category", imgpath ="Test image")
        url = reverse('course-create')
        valid_data = {
            "name": "Test name",
            "description": "Test description",
            "logo": "Test logo",
            "category": 1,
            "contacts": [
                {
                    "contact_type": 1,
                    "value": "Test value"
                }
            ],
            "branches": [
                {
                    "latitude": "Test latitude",
                    "longitude": "Test longitude",
                    "address": "Test address"
                }
            ]
        }
        response = self.client.post(url, json.dumps(valid_data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
