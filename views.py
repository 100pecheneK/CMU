from django.http import JsonResponse, HttpResponseRedirect
from .services.cutUrl import CutMyUrl


def register_url(request):
    if request.POST.get('action') == 'post':

        cmu_obj_url = request.POST.get('cmu_obj_url')
        cmu_new_url = CutMyUrl.get_short_url(url=cmu_obj_url)

        response_data = {
            'cmu_new_url': cmu_new_url,
        }

        return JsonResponse(response_data)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def redirect_page(request, obj_id):
    obj_url = CutMyUrl.get_object_url(obj_id=obj_id)
    return HttpResponseRedirect(obj_url)
