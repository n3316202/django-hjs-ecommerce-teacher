from django.shortcuts import render

# Create your views here.


# dev_9
def login_user(request):
    return (request, "accounts/login.html", {})
