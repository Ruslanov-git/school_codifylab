from django.urls import path
from students_app.views import StudentsViewSet


urlpatterns = [
    path('', StudentsViewSet.as_view({'get': 'list'}), name='students-list')
]