from django.urls import path
from .views import StudentListView
from .views import ClassperiodListView
from .views import TeacherListView
from .views import CourseListView
from .views import ClassroomListView
from .views import StudentDetailView
from .views import TeacherDetailView
from .views import ClassroomDetailView
from .views import ClassperiodDetailView
from .views import CourseDetailView


urlpatterns = [
    path ("students/", StudentListView.as_view(), name= "student_list_view"),
    path("classperiod/", ClassperiodListView.as_view(), name="classperiod_list_view"),
    path("teacher/", TeacherListView.as_view(), name="teacher_list_view"),
    path("course/", CourseListView.as_view(), name="course_list_view"),
    path("classroom/", ClassroomListView.as_view(), name= "classroom_list_view"),
    path("students/<int:id>/",StudentDetailView.as_view(),name= "student_detail_view"),
    path("teacher/<int:id>/",TeacherDetailView.as_view(),name= "teacher_detail_view"),
    path("classroom/<int:id>/",ClassroomDetailView.as_view(),name= "classroom_detail_view"),
    path("classperiod/<int:id>/",ClassperiodDetailView.as_view(),name= "classperiod_detail_view"),
    path("course/<int:id>/",CourseDetailView.as_view(),name= "course_detail_view")   
   
]