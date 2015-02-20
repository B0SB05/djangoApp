from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
    # Examples:
     url(r'^$', views.post_list, name='Home'),
     url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail,name='post_detail'),
     url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit,name='post_edit'),
     url(r'^post/new/$', views.post_new,name='post_new'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^admin/', include(admin.site.urls)),
    #url(r'', include('blog.urls')),
)
