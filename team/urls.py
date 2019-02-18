from django.conf.urls import url
from team import views

urlpatterns = [
    url(r'^$', views.team, name='team'),
]