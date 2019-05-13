from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(regex=r'^articles/',
        view=include('langscape.articles.urls', namespace='articles')),
    url(regex=r'^admin/',
        view=admin.site.urls),
]
