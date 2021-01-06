"""DASHBOARD URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include
from django.conf.urls.static import static
from .views import authenticate_user
from .settings import MEDIA_URL, MEDIA_ROOT

urlpatterns = [
    url(r'^authenticate_user/$', authenticate_user, name='authenticate_user'),
    # Django App URL(s)
    url(u'^links/', include('links.urls')),
] + static(MEDIA_URL, document_root=MEDIA_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)
