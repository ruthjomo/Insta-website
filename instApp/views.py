from django.shortcuts import render
from django.http  import HttpResponse
from django.http import HttpResponseRedirect

from .forms import NameForm


# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to Instagram website')


def get_name(request):

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'sign.html', {'form': form})    



