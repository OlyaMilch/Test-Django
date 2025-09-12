from django.contrib import admin
from django.urls import path, include


# It is a central route manager that reconciles all requests to the desired applications.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('cars.urls'))  # all routes will start with /api/
]
