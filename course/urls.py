from django.urls import path
from .views import CourseListAPIView, CourseCreateAPIView, DetailCourseView, CourseDeleteAPIView

urlpatterns = [
    path('', CourseListAPIView.as_view(), name='courses'),
    path('<int:pk>/', DetailCourseView.as_view(), name='course-detail'),
    path('create/', CourseCreateAPIView.as_view(), name='course-create'),
    path('delete/<int:pk>/', CourseDeleteAPIView.as_view(), name='course-delete'),   
]
