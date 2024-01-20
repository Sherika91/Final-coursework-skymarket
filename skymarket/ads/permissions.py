from rest_framework import permissions

from users.models import UserRoles


class IsOwnerOrAdmin(permissions.BasePermission):
    """ Custom permission to only allow owners of an object to edit it and allow read-only for others. """
    def has_object_permission(self, request, view, obj):
        # Checking if user has Logged in
        if request.user.is_authenticated:
            # Checking if user is owner of the object or admin
            if request.user == obj.author or request.user.role in [UserRoles.ADMIN]:
                return True
        return False
