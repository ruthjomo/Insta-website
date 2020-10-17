from django.conf.urls import url
from django.urls import path ,include
from .views import PostListView


app_name = "instApp"

urlpatterns =[
    url('',PostListView.as_view(),name='post_list'),
]
