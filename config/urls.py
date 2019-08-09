from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from rest_framework import routers

from langscape.api.views import ArticleListAPIView

router = routers.DefaultRouter()
router.register(r'articles', ArticleListAPIView)

urlpatterns = [
    url(r'',
        include('langscape.articles.urls', namespace='articles')),
    url(r'^about/',
        TemplateView.as_view(template_name="about.html")),
    url(r'^admin/',
        admin.site.urls),
    url('api/',
        include(router.urls)),
]
