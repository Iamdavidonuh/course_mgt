from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from accounts.models import CustomUser


class BaseUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["username", "email", "password"]

    def validate_password(self, value: str) -> str:
        """Hash value passed by user.
        :param value: password of a user
        :returns: a hashed version of the password
        """

        return make_password(value)


class StudentRegistrationSerializer(BaseUserSerializer):
    def create(self, validated_data):
        user = super().create(validated_data)
        user.is_student = True
        user.save()
        return user


class TeacherRegistrationSerializer(BaseUserSerializer):
    def create(self, validated_data):
        user = super().create(validated_data)
        user.is_teacher = True
        user.save()
        return user
