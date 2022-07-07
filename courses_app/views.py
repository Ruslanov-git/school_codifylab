from courses_app.models import Course
from courses_app.serializers import CourseSerializers
from rest_framework import viewsets


class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    """Он предоставляет информацию про курсы фронту"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializers

