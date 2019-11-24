from django.views import View


class LoginView(View):
    def get(self, request):
        pass

    def post(self, request):
        pass


def login_view(request):
    if request.method == "GET":
        pass
    elif request.method == "POST":
        pass
