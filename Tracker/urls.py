from django.urls import re_path
from .views import *


urlpatterns = [
    # re_path('^admin/', admin.site.urls),
    re_path(r'^$', index, name='index'),
    re_path(r'^delete_task/(?P<pk>\d+)$', delete_task, name='delete_task'),
]
