from django.contrib.auth import logout
from django.http import JsonResponse, HttpResponseRedirect


def healthcheck(request):
    return JsonResponse({"status": "UP"})


def logout_page(request):
    logout(request)
    return HttpResponseRedirect("/")
