from unicodedata import category
from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories


# Create your views here.
def index(request) -> HttpResponse:

    categories = Categories.objects.all()

    context = {
        "title": "Home - main",
        "content": "Furniture and accessories",
        "categories": categories,
    }
    return render(request, "main/index.html", context)


def about(request):
    context = {
        "title": "about",
        "content": "About page",
        "text_on_page": "Раздел «О нас» дает посетителям сайта представление о компании или личности. Цифры, кейсы, ссылки на крупных заказчиков — подтвержденная информация повышает ваш авторитет и формирует доверие со стороны аудитории. Здесь вы показываете свою значимость и объясняете, почему выгодно быть вашим клиентом.Этот раздел подходит для краткого рассказа о команде и истории развития компании. Покажите лица, которые стоят за продуктом — открытость расположит к вам людей. Раскройте свою миссию. Например, вы не просто торгуете техникой, а имеете цель — облегчить быт и улучшить качество жизни. Если есть награды и сертификаты, разместите их здесь.Есть вероятность, что сайт могут найти по ключевикам на странице, описывающей вашу деятельность. Учитывайте это при составлении текста. Возможно, вам пригодится этот материал: «SEO-текст: как писать оптимизированные и полезные статьи». Постарайтесь также, чтобы его было интересно читать. Чем больше времени пользователь проведет у вас, тем лучше будет позиция сайта в выдаче.",
    }
    return render(request, "main/about.html", context)
