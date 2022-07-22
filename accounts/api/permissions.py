from rest_framework.permissions import BasePermission


class IsStudent(BasePermission):
    """
    Allows access only to authenticated students.
    """

    def has_permission(self, request, view):
        return bool(
            request.user and request.user.is_authenticated and request.user.is_student
        )


class IsTeacher(BasePermission):
    """
    Allows access only to authenticated students.
    """

    def has_permission(self, request, view):
        return bool(
            request.user and request.user.is_authenticated and request.user.is_teacher
        )
