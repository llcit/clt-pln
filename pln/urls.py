from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.apps, name='apps'),
    url(r'^functions/$', views.functions, name='functions'),
    url(r'^formats/$', views.formats, name='formats'),
    url(r'^applications/$', views.applications, name='applications'),

    url(r'^app/(?P<item_id>[0-9]+)/$', views.app, name='app'),
    url(r'^app/new/$', views.app_new, name='app_new'),
    url(r'^app/(?P<item_id>[0-9]+)/edit/$', views.app_edit, name='app_edit'),
    url(r'^app/(?P<item_id>[0-9]+)/delete/$', views.app_delete, name='app_delete'),

    url(r'^format/(?P<item_id>[0-9]+)/$', views.format, name='format'),
    url(r'^format/new/$', views.format_new, name='format_new'),
    url(r'^format/(?P<item_id>[0-9]+)/edit/$', views.format_edit, name='format_edit'),
    url(r'^format/(?P<item_id>[0-9]+)/delete/$', views.format_delete, name='format_delete'),

    url(r'^function/(?P<item_id>[0-9]+)/$', views.function, name='function'),
    url(r'^function/new/$', views.function_new, name='function_new'),
    url(r'^function/(?P<item_id>[0-9]+)/edit/$', views.function_edit, name='function_edit'),
    url(r'^function/(?P<item_id>[0-9]+)/delete/$', views.function_delete, name='function_delete'),

    url(r'^application/(?P<item_id>[0-9]+)/$', views.application, name='application'),
    url(r'^application/new/$', views.application_new, name='application_new'),
    url(r'^application/(?P<item_id>[0-9]+)/edit/$', views.application_edit, name='application_edit'),
    url(r'^application/(?P<item_id>[0-9]+)/delete/$', views.application_delete, name='application_delete'),

    url(r'^applications/$', views.applications, name='applications'),
    url(r'^formats/$', views.formats, name='formats'),
    url(r'^functions/$', views.functions, name='functions'),
]
