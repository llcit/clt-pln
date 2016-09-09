from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.apps, name='apps'),
    url(r'^functions/$', views.functions, name='functions'),
    url(r'^formats/$', views.formats, name='formats'),
    url(r'^types/$', views.types, name='types'),

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

    url(r'^type/(?P<item_id>[0-9]+)/$', views.type, name='type'),
    url(r'^type/new/$', views.type_new, name='type_new'),
    url(r'^type/(?P<item_id>[0-9]+)/edit/$', views.type_edit, name='type_edit'),
    url(r'^type/(?P<item_id>[0-9]+)/delete/$', views.type_delete, name='type_delete'),

    url(r'^masonry', views.masonry, name='mansory'),
    url(r'^functions/$', views.functions, name='functions'),
    url(r'^formats/$', views.formats, name='formats'),
    url(r'^types/$', views.types, name='types'),
]
