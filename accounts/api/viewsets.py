from django.shortcuts import get_object_or_404
from rest_framework import viewsets, mixins, permissions, views, response
from accounts.api.permissions import IsTeacher
from accounts.api import serializers
from accounts.models import CustomUser


class AddStudentsViewset(viewsets.GenericViewSet, mixins.CreateModelMixin):
    serializer_class = serializers.StudentRegistrationSerializer
    permission_classes = [IsTeacher]


class DeleteStudentView(views.APIView):
    permission_classes = [IsTeacher]

    def delete(self, request, pk, format=None, **kwargs):
        student = get_object_or_404(CustomUser.objects.filter(is_student=True), pk=pk)
        student.delete()
        return response.Response({"status": "success"})


class TeacherRegistrationViewset(viewsets.GenericViewSet, mixins.CreateModelMixin):
    serializer_class = serializers.TeacherRegistrationSerializer
    permission_classes = [permissions.AllowAny]
