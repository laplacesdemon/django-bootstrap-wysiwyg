from django.conf.urls import patterns, include, url
from .views import MessageCreateView, MessageUpdateView, MultipleTextView

urlpatterns = patterns('',
    url(r'^$', MessageCreateView.as_view(), name='message-create'),
    url(r'^message/(?P<pk>[\w.@+-]+)/$', MessageUpdateView.as_view(), name='message-update'),
    url(r'^multiple$', MultipleTextView.as_view(), name='multiple-text'),
)
