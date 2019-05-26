from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(regex=r'^articles/',
        view=include('langscape.articles.urls', namespace='articles')),
    url(regex=r'^about/',
        view=TemplateView.as_view(template_name="about.html")),
    url(regex=r'^admin/',
        view=admin.site.urls),
]
