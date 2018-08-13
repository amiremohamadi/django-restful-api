from django.contrib import admin
from django.urls import re_path, include

from ServerRestAPI import urls as api_urls


urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^api/', include(api_urls)),
]