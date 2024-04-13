from django.urls import re_path
from .views import *

urlpatterns = [
    # re_path('^admin/', admin.site.urls),
    re_path(r'^$', index, name='index'),
    re_path(r'^delete_task/(?P<pk>\d+)$', delete_task, name='delete_task'),
    re_path(r'^search_task/$', search_task, name='search_task'),
    re_path(r'^edit_task/(?P<pk>\d+)$', edit_task, name='edit_task'),
    re_path(r'^complete_task/(?P<pk>\d+)$', complete_task, name='complete_task'),

]
