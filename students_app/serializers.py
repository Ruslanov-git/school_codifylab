from students_app.models import Student
from rest_framework import serializers


class StudentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
