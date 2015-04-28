from django.conf.urls import include, url
from remote.views import *

urlpatterns = [
    # Examples:
    # url(r'^$', 'omxwebremote.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^player/', player, name="player"),
    url(r'^ajax-remote/', ajax_remote, name="ajax-remote"),
    url(r'^explorer(.*)$', explorer, name="explorer"),
    url(r'^display(.*)$', display, name="display"),
]
