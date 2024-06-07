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


def products_page_view(request, page):
    if request.method == "GET":
        if isinstance(page, str):
            for data in DATABASE.values():
                if data['html'] == page:
                    with open(f'store/products/{page}.html', encoding="utf-8") as f:
                        data = f.read()
                    return HttpResponse(data)
        elif isinstance(page, int):
            data = DATABASE.get(str(page))  # Получаем какой странице соответствует данный id
            if data:  # Если по данному page было найдено значение
                with open(f'store/products/{data["html"]}.html', encoding="utf-8") as f:
                    data = f.read()
                return HttpResponse(data)

        return HttpResponse(status=404)
