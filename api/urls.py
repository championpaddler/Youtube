from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView,detail

urlpatterns = {
    url(r'^videos/$', CreateView.as_view()),
    url(r'^results/', detail, name='results'),

}

urlpatterns = format_suffix_patterns(urlpatterns)