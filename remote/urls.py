from django.conf.urls import include, url
from remote.views import *

urlpatterns = [
    # Examples:
    # url(r'^$', 'omxwebremote.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^main$', main, name="main"),
    url(r'^launch$', launch, name="launch"),
    url(r'^pause$', pause, name="pause"),
    url(r'^play$', play, name="play"),
]
