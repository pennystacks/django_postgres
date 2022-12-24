from django.forms import model_to_dict
from django.http import JsonResponse, HttpResponseNotFound, HttpResponseBadRequest
from django.core.serializers import serialize
from json import loads
from .models import BenchmarkUser


def json(request):
    return JsonResponse({"hello": "world", "foo": "bar"})


def profile(request, id):
    found = BenchmarkUser.objects.get(pk=id)

    if found is None:
        return HttpResponseNotFound()

    return JsonResponse(model_to_dict(found))


def users(request, page):
    if request.method == "GET":
        start = (page - 1) * 10
        found = BenchmarkUser.objects.all()[start:start+10]
        # data = serialize("json", found)
        res = [{"email": user.email, "id": user.pk, "name": user.name, "isAdmin": user.is_admin} for user in found]

        return JsonResponse(res, safe=False)

    return HttpResponseBadRequest()


def users_post(request):
    body = loads(request.body)
    new_user = BenchmarkUser(**body)
    new_user.save()

    return JsonResponse({"id": new_user.pk, "name": new_user.name, "email": new_user.email, "isAdmin": new_user.is_admin})