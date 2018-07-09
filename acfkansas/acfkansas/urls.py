"""acfkansas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url,include
from django.conf.urls.static import static
from django.contrib import admin
from . import settings
from core import views

urlpatterns = [
    url(r'^core/', include('core.urls', namespace='core')),
    url(r'^profiles/', include('profiles.urls', namespace='profiles')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'), 
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^summernote/', include('django_summernote.urls')),

    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)