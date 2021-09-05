from django.conf.urls import url
from djangoProject import views

urlpatterns = [
    url(r'^customers/$', views.customer_list),
    url(r'^customers/(?P[0-9]+)$', views.customer_detail),
]