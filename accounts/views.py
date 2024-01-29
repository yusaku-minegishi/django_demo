from django.contrib.auth import login, logout
from django.shortcuts import render, redirect

from .forms import LoginForm, SignUpForm


def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("sns:top")
    else:
        form = SignUpForm()
    param = {"form": form}
    return render(request, "accounts/signup.html", param)

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user:
                login(request, user)
                return redirect(to="sns:list")
    else:
        form = LoginForm()
    param = {"form": form}
    return render(request, "accounts/login.html", param)

def logout_view(request):
    logout(request)
    return render(request, "accounts/logout.html")
