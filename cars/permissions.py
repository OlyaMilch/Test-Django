from rest_framework.permissions import BasePermission, SAFE_METHODS


"""
Here are custom rights
For Country, Manufacturer, Car:
- GET always available to everyone.
- POST, PUT, DELETE — only by token.
"""


class IsAuthenticatedOrReadOnlyForUnsafe(BasePermission):

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:  # GET, HEAD, OPTIONS
            return True
        return request.user and request.user.is_authenticated


"""
For Comment:
- GET и POST always available to everyone.
- PUT и DELETE — only by token.
"""


class CommentPermission(BasePermission):

    def has_permission(self, request, view):
        if request.method in ('GET', 'POST'):
            return True
        return request.user and request.user.is_authenticated
