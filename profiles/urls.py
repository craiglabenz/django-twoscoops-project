from django.conf.urls import patterns, url
from views import user_profile

urlpatterns = patterns('',
    url(r'^me$', user_profile, name='user_profile'),
)