# Blog app urls
from django.conf.urls import url
from . import views

# Blog patterns
urlpatterns = [
    # View post_list
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
]
