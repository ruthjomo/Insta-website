from django.shortcuts import render
from .forms import PostForm
from .models import Post
from django.views.generic import ListView,CreateView
# Create your views here.

class PostListView(ListView):
    template_name = "post_list.html"
    queryset = Post.objects.all()
    context_object_name = "posts"

class PostCreateView(CreateView) :
    template = "/post_create.html" 
    from_class = PostForm 
    queryset = post.objects.all()
    #To return users to main page after every post
    success_url = '/'

    def form_valid(self,form):
        print(form.cleaned_data)
        #To prevent user from inputting their name every time they want to make a post
        form.instance.author = self.request.user
        return super().form_valid(form)
