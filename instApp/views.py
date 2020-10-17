from django.contrib.auth import login, authenticate
from . forms import  SignUpForm
from django.shortcuts import render ,redirect
from django.http  import HttpResponse





# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to Instagram website')

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


