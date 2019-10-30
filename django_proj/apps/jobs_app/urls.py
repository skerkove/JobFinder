from django.conf.urls import url
from . import views

                    
urlpatterns = [
    url(r'^home$', views.index),
    url(r'^python$', views.python),
    url(r'^process$', views.process),

   
]