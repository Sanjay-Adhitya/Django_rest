from django.contrib import admin
from django.conf.urls import url
from core import views 
urlpatterns = [
    url(r'fund/$', views.fundservice),
    url(r'fund/([0-9]+)$',views.fundservice),
    url(r'member/$',views.memberservice),
    url(r'member/([0-9]+)$',views.memberservice),
]
