from django.forms import model_to_dict
from django.http import JsonResponse


class CRUDView:
    model = None

    def retrieve(self, request, pk):
        instance = self.model.objects.get(pk=pk)
        return JsonResponse(model_to_dict(instance))

    def list(self, request):
        instances = self.model.objects.all()
        return JsonResponse(list(instances.values()), safe=False)

    @classmethod
    def urls(cls):
        def view(request, **kwargs):
            view = cls()
            if request.method == "GET":
                if "pk" in kwargs:
                    return view.retrieve(request, kwargs["pk"])
                else:
                    return view.list(request)
            else:
                return JsonResponse({"error": "Method not allowed"}, status=405)

        return view
