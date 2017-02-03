"""APISeries URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import RedirectView


from rest_framework import routers
from Series import views

from allauth.account.views import ConfirmEmailView

router = routers.DefaultRouter()
router.register(r'actors', views.actorViewSet)
router.register(r'series', views.serieViewSet)
router.register(r'users', views.UserList)


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
    # url(r'^serie/', include('Series.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^rest-auth/registration/account-confirm-email/(?P<key>[-:\w]+)/$', ConfirmEmailView.as_view(), name='account_email'),
    url(r'^accounts/', include('allauth.urls')),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
