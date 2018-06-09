from django.http import HttpResponse, JsonResponse
import json


card = []
products = dict({
        "1000": {
            "owner": "system",
            "type": "الیاف طبیعی",
            "contain": "کلاه¡ زير دکمه دار آستين کوتاه",
            "age": "سه تا شش ماهگي",
            "imgURL": "http://www.yourtradepubs.com/wp-content/uploads/2018/03/shabby-chic-baby-girl-clothes-best-of-buy-grey-unicorn-skirt-braces-t-shirt-set-3mths-6yrs-from-the-of-shabby-chic-baby-girl-clothes.jpg",
            "location": "تهران",
            "id": "10u930uh17mjhgcyda2",
            "washable": "دستي¡ لباسشويي",
            "isPhysical": "0",
            "price": 96750,
            "appropriate": "بهار و تابستان",
            "hasBoughtPhone": True,
            "phone": "021-44808044",
            "description": "بدون ایجاد حساسیت برای پوست",
            "seller": "bonten"

        },
})


def index(request):
    return HttpResponse("Hello")


def profile(request):

    return JsonResponse({
        "code": 200,
        "data": {
            "name": "رضا",
            "balance": 2000,
            "phone": "021-44858075",
            "id": "10001000",
            "isAdmin": 1,
            "username": "reza",
        }
    })


def login(request):
    return JsonResponse({
        "code": 200,
        "data": {
            "user": {
                "balance": 2000,
                "name": "رضا",
                "id": "10001000"
            },
            "token": "111"
        },
        "message": "ورود موفقی آمیز بود"
    })


def search(request):
    pid = '1000'
    return JsonResponse({
        "code": 200,
        "data": [{
            "id": pid,
            "price": products[pid]['price'],
            "seller": products[pid]['seller'],
            "isPhysical": products[pid]['isPhysical'],
            "imgURL": products[pid]['imgURL'],
            "location": products[pid]['location']
        }],
        "message": "موفقیت"
    })


def product(request):
    return JsonResponse({
        "data": products['1000'],
        "code": 200,
        "message": "موفقیت"
    })


def charge(request):
    return JsonResponse({
        "code": 200,
        "message": "سفارش شما با موفقیت ثبت شد"
    })


def addToCard(request):
    param = json.loads(request.body)
    pid = param['id']
    card.append(pid)
    # print(products[str(pid)])
    print(card)

    return JsonResponse({
        "code": 200,
        "message": "کالای شما به سبد خرید اضافه شد",
    })