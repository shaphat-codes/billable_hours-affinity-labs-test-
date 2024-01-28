from django.contrib import admin
from django.urls import path
from timetracking.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/timetables', list_timetables),
    path('api/v1/timetable', create_timetable),
]
