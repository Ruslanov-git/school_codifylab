from courses_app.models import Course
from rest_framework.validators import UniqueTogetherValidator
from rest_framework import serializers


class CourseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['name', 'duration', 'price', 'is_active']

        """Такое можно сделать если к нам с фронта будет приходить информация, 
        если ничего не приходит, то нет, нужно записать в models"""
        # validators = [
        #     UniqueTogetherValidator(
        #         queryset=Course.objects.all(),
        #         fields=['name', 'duration', 'price']
        #     )
        # ]
