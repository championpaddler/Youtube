from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView

urlpatterns = {
    url(r'^videos/$', CreateView.as_view()),
}

urlpatterns = format_suffix_patterns(urlpatterns)