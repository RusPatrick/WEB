from django.conf.urls import url

from questions.views import BaseView

from . import views

urlpatterns = [
    url(r'^base', views.post_list, name='base'),
    url(r'index', views.post_list, name='index'),
]
