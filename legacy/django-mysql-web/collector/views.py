from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, "index.html", )


@login_required
def recorder(request):
    return render(request, "recorder.html", )


@login_required
def signout(request):
    logout(request)
    return HttpResponseRedirect(reverse('collector:index'))


def signup(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        print("in")

        if form.is_valid():
            print("out")
            new_user = form.save()
            authenticated_user = authenticate(username=new_user.username,
                                              password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('collector:recorder'))
    context={'form':form}
    return render(request, 'signup.html', context)
