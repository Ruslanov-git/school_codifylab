from django.db import models
from courses_app.models import Course


class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=14)
    email = models.EmailField()
    gender = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')))
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)

    class Meta:
        unique_together = (
            (
                'first_name',
                'last_name',
                'date_of_birth',
                'phone_number'
            ),
        )

    """ Первый способ сделать чтобы при записи ФИО 
    ФИО начиналось с заглавной буквы
    def save(self, *args, **kwargs):
        for field_name in ['first_name', 'last_name']:
            val = getattr(self, field_name, False)
            if val:
                setattr(self, field_name, val.capitalize())
        super(Student, self).save(*args, **kwargs)"""

    """Второй способ сделать чтобы при записи ФИО 
    ФИО начиналось с заглавной буквы"""
    def save(self, *args, **kwargs):
        self.first_name = self.first_name.capitalize()
        self.last_name = self.last_name.capitalize()
        super(Student, self).save(*args, **kwargs)

    def __str__(self):
        return self.first_name
