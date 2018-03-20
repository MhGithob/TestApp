from django.conf.urls.defaults import patterns, include, url
from . import view

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    url(r'^$', view.hello),
]
