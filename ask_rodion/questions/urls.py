from django.conf.urls import url

from questions.views import BaseView

urlpatterns = [
    url(r'^base', BaseView.as_view(), name='base'),
]