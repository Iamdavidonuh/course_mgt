from rest_framework import viewsets, mixins, permissions
from accounts.api import serializers


class StudentRegistrationViewset(viewsets.GenericViewSet, mixins.CreateModelMixin):
    serializer_class = serializers.StudentRegistrationSerializer
    permission_classes = [permissions.AllowAny]


class TeacherRegistrationViewset(viewsets.GenericViewSet, mixins.CreateModelMixin):
    serializer_class = serializers.TeacherRegistrationSerializer
    permission_classes = [permissions.AllowAny]
