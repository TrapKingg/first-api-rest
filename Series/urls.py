from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from Series import views

urlpatterns = [
    url(r'^actors/$', views.actorList.as_view()),
    url(r'^actors/(?P<pk>[0-9]+)/$', views.actorDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
