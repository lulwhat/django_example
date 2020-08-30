from django.conf.urls import url

from . import views

app_name = 'data'

urlpatterns = [
    url(r'^$', views.index1, name='index1'),
]