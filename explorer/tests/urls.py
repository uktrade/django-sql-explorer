from django.conf.urls import url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from explorer.urls import urlpatterns

admin.autodiscover()

urlpatterns += [
    url(r'^admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()
