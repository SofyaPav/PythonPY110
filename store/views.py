from django.http import JsonResponse
from .models import DATABASE
from django.http import HttpResponse, HttpResponseNotFound


def products_view(request):
    if request.method == "GET":
        id = request.GET.get('id')
        if id is None:
            return JsonResponse(DATABASE, json_dumps_params={'ensure_ascii': False,
                                                     'indent': 4})
        else:
            for v in DATABASE.values():
                if v['id'] == int(id):
                    return JsonResponse(v, json_dumps_params={'ensure_ascii': False,
                                                              'indent': 4})
            return HttpResponseNotFound("Данного продукта нет в базе данных")



def shop_view(request):
    if request.method == "GET":
        with open('store/shop.html', encoding="utf-8") as f:
            data = f.read()  # Читаем HTML файл
        return HttpResponse(data)  # Отправляем HTML файл как ответ