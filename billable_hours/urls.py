from django.contrib import admin
from django.urls import path, include
from timetracking.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/timetable', create_timetable),
]
