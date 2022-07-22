from rest_framework import viewsets, mixins
from accounts.api import permissions as account_permissions
from courses.api import serializers
from courses import models


class SubjectCreationViewset(viewsets.ModelViewSet):

    permission_classes = [account_permissions.IsTeacher]
    serializer_class = serializers.SubjectSerializer

    queryset = models.Subject.objects.all()


class CourseCreationViewset(viewsets.ModelViewSet):

    permission_classes = [account_permissions.IsTeacher]
    serializer_class = serializers.CourseCreationSerializer

    queryset = models.Course.objects.all()


class ModuleCreationViewset(viewsets.ModelViewSet):

    permission_classes = [account_permissions.IsTeacher]
    serializer_class = serializers.ModuleCreationSerializer

    queryset = models.Module.objects.all()
