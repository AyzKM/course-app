from rest_framework import status
from django.http import response
from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
import json
from course.models import Course, Category
from course.serializers import CourseSerializer

client = APIClient()

class CourseViewsTestCase(TestCase):
    def setUp(self):
        self.url = reverse('courses')
        self.valid_data = {
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
							"longitude": "Test longtitude",
							"address": "Test adress"
						}
					]
				}

    def test_courselist_loads_success(self):
        response = client.get(self.url)
        course_list = Course.objects.all()
        serializer = CourseSerializer(course_list, many=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)

    def test_get_detail_view_success(self):
        category = Category.objects.create(name = "Test category", imgpath = "Test image")
        course = Course.objects.create(name = "Test name", description = "Test description", logo = "Test logo", category = category)
        response = client.get(reverse('course-detail', kwargs={'pk': course.pk}))
        course = Course.objects.get(pk=course.pk)
        serializer = CourseSerializer(course)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)

    def test_delete_view_success(self):
        category = Category.objects.create(name = "Testcategory", imgpath = "Testimage")
        course = Course.objects.create(name="Testname", description="Testdescription", logo ="Testlogo", category = category)
        response = client.delete(reverse('course-delete', kwargs={'pk': course.pk}))
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_get_detail_view_invalid(self):
        response = client.get(reverse('course-detail', kwargs={'pk': 23}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

#not working
    def test_create_view_success(self):
        response = self.client.post(reverse('course-create'), data=json.dumps(self.valid_data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
