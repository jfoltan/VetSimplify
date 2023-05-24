from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistrationForm

# Create your views here.


def sign_up(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("records:owner_list")
    else:
        form = RegistrationForm()

    return render(request, "registration/sign_up.html", {"form": form})
