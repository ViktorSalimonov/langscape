from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^articles/',
        include('langscape.articles.urls', namespace='articles')),
    url(r'^about/',
        TemplateView.as_view(template_name="about.html")),
    url(r'^admin/',
        admin.site.urls),
]
