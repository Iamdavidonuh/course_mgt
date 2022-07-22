from django.urls import path, include

from rest_framework import routers
from accounts.api import viewsets

router = routers.DefaultRouter()

router.register(
    "register/student", viewsets.StudentRegistrationViewset, basename="student-reg"
)
router.register(
    "register/teacher", viewsets.TeacherRegistrationViewset, basename="teacher-reg"
)

urlpatterns = [
    path("api/", include(router.urls)),
]
