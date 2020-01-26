from django.urls import reverse_lazy

from ..models import CMU


class CutMyUrl:
    @classmethod
    def get_short_url(self, url):
        obj = self.save_url_to_db(url)
        # TODO: Изменить ссылку!!! new_url
        new_url = f'http://127.0.0.1:8000{reverse_lazy("cmu:redirect_page", args=(obj.id,))}'
        return new_url

    @classmethod
    def get_object_url(self, obj_id):
        obj = CMU.objects.get(id=obj_id)
        return obj.object_url

    @classmethod
    def save_url_to_db(self, url):
        try:
            obj = CMU.objects.get(object_url=url)
        except CMU.DoesNotExist:
            url = url
            obj = CMU.objects.create(object_url=url)
        return obj
