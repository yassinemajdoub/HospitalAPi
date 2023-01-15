from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied


class IsProvider(BasePermission):
    def has_permission(self, request, view):
        if not request.user :
            raise PermissionDenied(detail="cannot identify user.")
        elif not request.user.is_provider:    
            raise PermissionDenied(detail="Only providers are allowed to perform this action.")
        return True

    def has_object_permission(self, request, view, obj):
        # Allow providers to perform GET, PATCH, and POST requests
        if request.method in ["GET", "PATCH", "POST"]:
            return True
        # For all other methods (e.g. DELETE), raise a permission denied exception
        raise PermissionDenied(detail="providers are not allowed to Delete information ")
