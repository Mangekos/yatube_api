from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Изменение чтение и объектов.

    Только автор может изменить объект, стальным доступно чтение.
    """

    def has_object_permission(self, request, view, obj):
        return bool(
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )
