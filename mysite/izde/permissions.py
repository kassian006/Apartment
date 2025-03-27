from  rest_framework import permissions


class CheckUser(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.status == 'admin':
            return True
        return False