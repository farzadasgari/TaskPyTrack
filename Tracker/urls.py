from django.urls import re_path
from .views import *


urlpatterns = [
    # re_path('^admin/', admin.site.urls),
    re_path(r'^$', index, name='index'),
]
