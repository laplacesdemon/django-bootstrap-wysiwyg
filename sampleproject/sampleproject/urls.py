from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^', include('demo.urls', namespace='demo')),
)
