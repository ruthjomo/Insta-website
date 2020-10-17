from django.contrib.auth import login, authenticate
from . forms import  SignUpForm
from django.shortcuts import render ,redirect
from django.http  import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
import datetime as dt





# Create your views here.
# def welcome(request):
#     return HttpResponse('Welcome to Instagram website')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})  

def get_object(self):
        id_ = self.kwargs.get("username")
        user = get_object_or_404(User, username=id_)
        posts = user.posts.all()
        return user

def get_context_data(self, *args, **kwargs):
    context = super(Profile,self).get_context_data(*args, **kwargs)
    user = self.get_object()
    context.update({
    'posts' :          user.posts.all().filter(created_date__lte=timezone.now()).order_by(' -created_date')
 })
    return context      


