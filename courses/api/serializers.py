from rest_framework import serializers
from accounts.models import CustomUser
from courses import models


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Subject
        fields = "__all__"


class CourseCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = "__all__"


class ModuleCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Module
        fields = "__all__"
