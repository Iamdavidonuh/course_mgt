from django.urls import path, include

from rest_framework import routers
from courses.api import viewsets

router = routers.DefaultRouter()

router.register("subject", viewsets.SubjectCreationViewset, basename="subject")
router.register("course", viewsets.CourseCreationViewset, basename="course")
router.register("module", viewsets.ModuleCreationViewset, basename="module")


urlpatterns = [
    path("api/", include(router.urls)),
]
