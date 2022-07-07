from students_app.models import Student
from students_app.serializers import StudentsSerializers
from rest_framework import viewsets


class StudentsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentsSerializers
