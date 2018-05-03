from django.conf.urls import url
from .import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns =[
    url(r'^archive/$', views.archive, name="archive"),
    url(r'^contact/$', views.contact, name="contact"),
    url(r'^$',views.post_list,name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
]   + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
