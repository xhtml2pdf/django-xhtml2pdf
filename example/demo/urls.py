"""demo URL Configuration

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
from django.contrib import admin
from views import test_view, test_render_response, UserPdfView, \
        render_template_decorated, test_view_fileobject

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^test_view$', test_view),
    url(r'^test_render_response$', test_render_response),
    url(r'^test_view_fileobject$', test_view_fileobject),
    url(r'^test_user/(?P<pk>\d+)$', UserPdfView.as_view()),
    url(r'^render_template_decorated$', render_template_decorated)
]

