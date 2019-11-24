from django.views import View
from django.shortcuts import render
from . import forms


class LoginView(View):
    def get(self, request):
        form = forms.LoginForm(initial={"email": "jinaganda5@gmail.com"})
        return render(request, "users/login.html", {"form": form})

    def post(self, request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            print(
                form.cleaned_data
            )  # if clean_Ftn would not return anything, change data that post in templates to None.
        return render(request, "users/login.html", {"form": form})


# CSRF
# not our website, another site access to our wevsite login with marvelous button
# because we have cookie
# so this problem is solved by django csrf token.

