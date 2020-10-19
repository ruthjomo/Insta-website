from django.conf.urls import url
from django.urls import path ,include
from .views import PostListView,PostCreateView,


app_name = "instApp"

urlpatterns =[
    url('',PostListView.as_view(),name='post_list'),
    url('new/',PostCreateView.as_view(),name='post_new'),
]
