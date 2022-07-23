from django.shortcuts import get_object_or_404
from rest_framework import viewsets, mixins, views, response, exceptions
from rest_framework.decorators import action
from accounts.api import permissions as account_permissions
from accounts.models import CustomUser
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


class CourseEnrollView(views.APIView):
    permission_classes = [account_permissions.IsStudent]

    def post(self, request, pk, format=None):
        course = get_object_or_404(models.Course, pk=pk)
        course.students.add(request.user)
        return response.Response({"enrolled": True})


class StudentsInCourse(views.APIView):
    permission_classes = [account_permissions.IsTeacher]

    def get(self, request, pk, format=None):
        course = get_object_or_404(models.Course, pk=pk)
        students = course.students.all()
        serializer = serializers.StudentSerializer(students, many=True)
        return response.Response({"students": serializer.data})


class CompleteCourse(views.APIView):
    permission_classes = [account_permissions.IsStudent]

    def post(self, request, pk, format=None):
        course = get_object_or_404(models.Course, pk=pk)
        completed_table, _ = models.StudentCourseCompletion.objects.get_or_create(
            student=self.request.user
        )
        completed_table.course.add(course)
        return response.Response({"completed": True})


class ListCompletedCourseStudents(views.APIView):
    """returns a list of students who has completed a particular course"""

    permission_classes = [account_permissions.IsTeacher]

    def get(self, request, pk, format=None):
        course = get_object_or_404(models.Course, pk=pk)

        data = models.StudentCourseCompletion.objects.filter(course=course).all()
        serializer = serializers.StudentCourseCompletionSerializer(data, many=True)
        return response.Response({"students": serializer.data})


class RemoveStudentFromCourseView(views.APIView):

    permission_classes = [account_permissions.IsTeacher]

    def post(self, request, pk, format=None, **kwargs):
        student = get_object_or_404(
            CustomUser.objects.filter(is_student=True),
            pk=self.kwargs["student_pk"],
        )
        course = get_object_or_404(models.Course, pk=pk)
        course.students.remove(student)
        return response.Response({"status": "success"})


class AddStudentToCourseView(views.APIView):

    permission_classes = [account_permissions.IsTeacher]

    def post(self, request, pk, format=None, **kwargs):
        student = get_object_or_404(
            CustomUser.objects.filter(is_student=True),
            pk=self.kwargs["student_pk"],
        )
        course = get_object_or_404(models.Course, pk=pk)
        course.students.add(student)
        return response.Response({"status": "success"})
