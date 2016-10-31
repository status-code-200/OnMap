from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views


urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^$', 'web.views.index'),
    url(r'^home/$', 'web.views.home'),
    url(r'^logout/$', 'web.views.logout'),
)
