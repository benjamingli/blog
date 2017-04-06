"""blog URL Configuration

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
from django.contrib import admin
from my_blog import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.home,name="home"),
    url(r'^message/$',views.message,name="message"),
    url(r'^about/$',views.about,name="about"),
    url(r'^archive/$',views.archive,name="archive"),
    url(r'^search/$',views.blog_search,name='search'),
    url(r'^submiting/$',views.submiting,name="submiting"),
    url(r'^submit_done/$',views.submit_done,name="submit_done"),
    url(r'^article/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<id>\d+)/$',views.detail,name="detail"),
]+ static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
