from home.models import *
from django.db.models import Q

CHARS = 'qwertyuiopasdfghjklzxcvbnm'

def user_serializer(o: User):
    return {
            'id': o.pk, 
            'first_name': o.first_name, 
            'last_name': o.last_name, 
            'phone': o.phone, 
            'img': o.img.url, 
            'diamond': o.diamond, 
        }


def product_serializer(o: Product):
    return {'id': o.id, 'shop_id': o.shop.id, 'images': [o.image1.url, o.image2.url if o.image2 else '', o.image3.url if o.image3 else '', ], 'name': o.name, 'description': o.description, 'count': o.count, 'money_type': o.currency, 'type': o.type, 'entry_price': o.entry_price, 'price': o.price, 'percent': o.percent, 'selling_price': o.selling_price, 'company': o.company, 'likes': [user_serializer(i) for i in o.likes.all()], "views": [user_serializer(i) for i in o.seens.all()]}

def eproduct_serializer(o: EProduct):
    return {'id': o.pk, 'shop_id': o.shop.id, 'images': [o.image1.url, o.image2.url if o.image2 else '', o.image3.url if o.image3 else '', ], 'name': o.name, 'money_type': o.currency, 'type': o.type, 'selling_price': o.selling_price, 'likes': [user_serializer(i) for i in o.likes.all()]}


def shop_serializer(shop: Shop):
    return {'host': user_serializer(shop.host), "admins": [user_serializer(admin) for admin in shop.admins.all()], "members": [user_serializer(member) for member in shop.members.all()], "products": [product_serializer(o) for o in Product.objects.filter(shop=shop)], "selected" : [product_serializer(o) for o in Product.objects.filter(Q(shop=shop) & Q(selected=True))], 'id': shop.pk, 'type': shop.type, 'name': shop.name, 'description': shop.bio, 'currency' : 'So\'m' if shop.currency == 0 else 'Dollar' , 'img': shop.image.url, 'viloyat': shop.viloyat.name, 'tuman': shop.tuman.name, 'location': {'lat': shop.lat, 'lon': shop.lon, }}

def check_promocode(code):
    for i in Promocode.objects.all():
        if i.code == code:
            return True
        
    return False