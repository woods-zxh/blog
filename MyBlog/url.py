from django.conf.urls import url

from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns =[
    url(r'^$', views.login1, name='login1'),
    url(r'^regist/$', views.regist, name='regist'),
    url(r'^index/$', views.index, name='index'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^show1/$',views.show1,name="show1"),
    url(r'^show2/$',views.show2,name="show2"),
    url(r'^show3/$',views.show3,name="show3"),
    url(r'^show4/$',views.show4,name="show4"),
    url(r'^comment/$',views.comment,name="comment"),
    url(r'^upload/$',views.uploadImg,name="upload"),
    url(r'^sigh/$', views.sigh, name="sigh"),
    url(r'^showing/$',views.showImg, name = "showing"),
    url(r'^write/$', views.write, name="write"),
    url(r'^delete/$', views.delete, name="delete"),
    url(r'^search/$', views.search, name="search"),
    url(r'^change/$', views.change, name="change"),
    url(r'^detail/(.+)/$', views.detail, name="detail"),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)