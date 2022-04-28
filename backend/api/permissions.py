from rest_framework import permissions
from rest_framework.permissions import DjangoModelPermissions


class IsStaffEditorPermission(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        user = request.user
        print(user.get_all_permissions())
        return True
