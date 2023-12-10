from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import User, Posts
from django.db import IntegrityError


def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    if request.method == "POST":
        post_content = request.POST["post-content"]
        new_post = Posts(text=post_content, author=request.user)
        new_post.save()
    return render(request, "profile.html", {"user": User.objects.get(username=request.user.username), "posts": Posts.objects.filter(author=request.user)})


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirm_password"]
        if password != confirmation:
            return render(request, "register.html", {
                "message": "Passwords must match."
            })
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
        except IntegrityError:
            return render(request, "register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "register.html")


@login_required
def edit(request):
    username = request.user
    user = User.objects.get(username=username)
    if request.method == "POST":
        profile_pic = request.POST["profile_pic"]
        email = request.POST["email"]
        facebook = request.POST["facebook"]
        github = request.POST["github"]
        linkedin = request.POST["linkedin"]
        twitter = request.POST["twitter"]
        faculty = request.POST["faculty"]
        country = request.POST["country"]

        user.profile_picture = profile_pic
        user.email = email
        user.facebook_account = facebook
        user.github_account = github
        user.linkedin_account = linkedin
        user.twitter_account = twitter
        user.faculty = faculty
        user.country = country

        user.save()
        return render(request, "profile.html", {"user": User.objects.get(username=request.user.username)})
    else:
        return render(request, "edit-profile.html")


