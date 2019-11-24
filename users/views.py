from django.views import View
from django.shortcuts import render
from . import forms


class LoginView(View):
    def get(self, request):
        form = forms.LoginForm(initial={"email": "jinaganda5@gmail.com"})
        return render(request, "users/login.html", {"form": form})

    def post(self, request):
        form = forms.LoginForm(request.POST)
        print(form.is_valid())  # if form is valid, return True
        return render(request, "users/login.html", {"form": form})


# CSRF
# not our website, another site access to our wevsite login with marvelous button
# because we have cookie
# so this problem is solved by django csrf token.

