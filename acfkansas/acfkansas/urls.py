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
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from . import views, settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'), 
    url(r'^(?P<about_type>[\w]+)/about$', views.about, name='about'),  
    url(r'^(?P<ministry_type>[\w]+)/ministry$', views.ministry , name='ministry'),   
    url(r'^contact/$', views.contact , name='contact'), 
    url(r'^(?P<resources_type>[\w]+)/resources$', views.resources , name='resources'), 
    url(r'^whatwedo/$', views.whatwedo , name='whatwedo'),
    url(r'^building/$', views.building , name='building'),
    url(r'^(?P<happening_type>[\w]+)/happening$', views.happening , name='happening'),
    url(r'^(?P<happeningdetail_type>[\w]+)/happeningdetail$', views.happeningdetail , name='happeningdetail'),

    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)