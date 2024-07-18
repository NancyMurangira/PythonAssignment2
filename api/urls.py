from django.urls import path
from .views import StudentView
from .views import ClassroomPeriodView
from .views import ClassesView
from .views import CoursesView
from .views import TeachersView
from .views import StudentDetailView

urlpatterns=[
    path("students/", StudentView.as_view(), name="student_view"),
    path("periods/", ClassroomPeriodView.as_view(), name="classroomPeriod_list_view"),
    path("classes/", ClassesView.as_view(), name="classes_list_view"),
    path("courses/", CoursesView.as_view(), name="courses_list_view"),
    path("courses/",TeachersView.as_view(), name="teacherslist_view"),
    path("students/<int:id>/" , StudentDetailView.as_view(),name= "student_detail_view"),

]