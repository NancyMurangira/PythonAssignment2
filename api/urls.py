from django.urls import path
from .views import StudentView
from .views import ClassPeriodView
from .views import ClassesView
from .views import CoursesView
from .views import TeachersView
from .views import StudentDetailView
from .views import ClassPeriodDetailView
from .views import TeacherDetailView
from .views import ClassDetailView
from .views import CourseDetailView

urlpatterns=[
    path("students/", StudentView.as_view(), name="student_view"),
    path("periods/", ClassPeriodView.as_view(), name="classPeriod_list_view"),
    path("classes/", ClassesView.as_view(), name="classes_list_view"),
    path("courses/", CoursesView.as_view(), name="courses_list_view"),
    path("teacher/",TeachersView.as_view(), name="teacherslist_view"),
    path("students/<int:id>/" , StudentDetailView.as_view(),name= "student_detail_view"),
    path("periods/<int:id>/" , ClassPeriodDetailView.as_view(),name= "classroom_detail_view"),
    path("classes/<int:id>/" , ClassDetailView.as_view(), name="class"),
    path("courses/<int:id>/" , CourseDetailView.as_view(), name="course"),
    path("teacher/<int:id>/" , TeacherDetailView.as_view(), name="teachers"),
]