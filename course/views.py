from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import  status
from .models import Course
from .serializers import CourseSerializer

class CourseListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(data=serializer.data)

class DetailCourseView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            course_object = Course.objects.get(pk=kwargs.get('pk'))
            serializer = CourseSerializer(instance=course_object)
            return Response(data=serializer.data)
        except Course.DoesNotExist as e:
            return Response(data=f"{e}", status=status.HTTP_404_NOT_FOUND)

class CourseCreateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.POST
        serializer = CourseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={'message': 'Course has been added successfully'}, status=201)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CourseDeleteAPIView(APIView):
    def delete(self, request, *args, **kwargs):
        course = Course.objects.get(pk=kwargs.get('pk'))
        course.delete()
        return Response(data={'message': 'Course has been successfully deletes'}, status=status.HTTP_204_NO_CONTENT)
