from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
     url(r'^signup/$',views.signup, name='signup'),
    
]