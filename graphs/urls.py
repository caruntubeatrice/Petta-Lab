from django.conf.urls import url
from . import views

urlpatterns = [
    # /graphs
    url(r'^$', views.Graph_home.as_view(), name='graphs'),
    # /graphs/press1/
    url(r'^press(?P<num>[0-9]+)/(?P<day>[0-9]+)$', views.plotPress, name='plotPressure'),
    # /graphs/temp1/
    url(r'^temp(?P<num>[0-9]+)/(?P<day>[0-9]+)/$', views.plotTemp, name='plotTemperature'),
    url(r'^temp(?P<num>[0-9]+)/?data=(?P<day>[0-9]+)/$', views.plotTemp, name='plotTemperature'),
]