from django.urls import path, include

from rest_framework import routers
from courses.api import viewsets

router = routers.DefaultRouter()

router.register("subject", viewsets.SubjectCreationViewset, basename="subject")
router.register("course", viewsets.CourseCreationViewset, basename="course")
router.register("module", viewsets.ModuleCreationViewset, basename="module")


urlpatterns = [
    path("api/", include(router.urls)),
    path(
        "courses/<pk>/enroll/",
        viewsets.CourseEnrollView.as_view(),
        name="course_enroll",
    ),
    path(
        "courses/<pk>/students/",
        viewsets.StudentsInCourse.as_view(),
        name="course_students",
    ),
    path(
        "courses/<pk>/complete/",
        viewsets.CompleteCourse.as_view(),
        name="course_completed",
    ),
    path(
        "courses/<pk>/complete/students",
        viewsets.ListCompletedCourseStudents.as_view(),
        name="course_students_completed",
    ),
    path(
        "courses/<pk>/student-remove/<student_pk>",
        viewsets.RemoveStudentFromCourseView.as_view(),
        name="course_student_remove",
    ),
    path(
        "courses/<pk>/student-add/<student_pk>",
        viewsets.AddStudentToCourseView.as_view(),
        name="course_student_add",
    ),
]
