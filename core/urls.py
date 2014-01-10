# Django
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin

# Local Apps
from profiles import views as profile_views

admin.autodiscover()
urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='base.html')),

    # General
    url(r'^logout$', profile_views.logout_view, name='logout'),

    # AllAuth
    (r'^accounts/', include('allauth.urls')),
    (r'^profiles/', include('profiles.urls')),

    # Admin
    url(r'^admin/', include(admin.site.urls)),
)
