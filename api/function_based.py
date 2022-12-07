from urllib import response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api import *
from home.models import *
from accounts.models import User

from rest_framework.request import Request
from geopy import distance




@api_view(['POST'])
def shop_add_member(request):

    user_id = request.data.get('user-id')
    shop_id = request.data.get('shop-id')

    try:
        user = User.objects.get(pk=user_id)
        shop = Shop.objects.get(pk=shop_id)

        shop.members.add(user)
        shop.save()
    except Exception as e:
        print('Error', e)
        print('Shop add member failed!')

    return Response({'status': 200} if user_id and shop_id else {'status': 400})


@api_view(['POST'])
def shop_add_admin(request):

    user_id = request.data.get('user-id')
    shop_id = request.data.get('shop-id')

    try:
        user = User.objects.get(pk=user_id)
        shop = Shop.objects.get(pk=shop_id)
        shop.admins.add(user)
        shop.save()
    except Exception as e:
        print('Error', e)
        print('Shop add admin failed!')
    return Response({'status': 200} if user_id and shop_id else {'status': 400})


@api_view(['POST'])
def report(request):
    rd = request.data
    try:
        new_report = Report.objects.create(
            type=rd['type'], product=Product.objects.get(pk=rd['product_id']))
    except Exception as e:
        print('Failed to create report')
    return Response({'status': 200})


@api_view(['GET'])
def like(request):
    product = Product.objects.get(pk=request.GET.get('product_id'))
    user = User.objects.get(pk=request.GET.get('user_id'))
    command = request.GET.get('command')
    if command == 'add':
        product.likes.add(user)
    elif command == 'remove':
        product.likes.remove(user)
    return Response({'status': 200})


@api_view(['GET'])
def check_like(request):
    product = Product.objects.get(pk=request.GET.get('product_id'))
    user = User.objects.get(pk=request.GET.get('user_id'))
    if product.likes.filter(id=user.id).exists():
        return Response({'status': 200})
    return Response({'status': 400})


@api_view(['POST'])
def change_owner(request):
    rd = request.data
    name = rd['name']
    password = rd['password']
    user_id = rd['user-id']

    try:
        shop = Shop.objects.get(name=name, password=password)
        user = User.objects.get(pk=user_id)

        shop.host = user

        shop.save()
    except Exception as e:
        print('Chane owner failed')

        return Response({'status': 400})
    return Response({'status': 200})


@api_view(['GET'])
def regions(request):
    response = {
        'status': 200,
        'data': []
    }
    for i in Region.objects.all():
        response['data'].append(
            {
                'id': i.id,
                'name': i.name
            }
        )

    return Response(response)


@api_view(['GET'])
def districts(request):
    response = {
        'status': 200,
        'data': []
    }

    region_id = request.GET.get('region-id')

    for i in District.objects.filter(region__id=region_id):
        response['data'].append(
            {
                'id': i.id,
                'region_id': i.region.id,
                'name': i.name,
            }
        )

    return Response(response)


@api_view(['GET'])
def chat_list(request):
    response = {
        'status': 200,
        'data': []
    }
    shop_id = request.GET.get('shop-id')

    for i in Chat.objects.filter(shop__id=shop_id):
        response['data'].append(
            {
                'id': i.id,
                'name': i.user.first_name,
                'img': i.user.img.url
            }
        )

    return Response(response)


@api_view(['GET'])
def messages(request):
    response = {
        'status': 200,
        'data': []
    }
    chat_id = request.GET.get('chat-id')

    for i in Message.objects.filter(chat__id=chat_id):
        dat = {
            'id' : i.pk,
            'sended_by_shop' : i.sended_by_shop,
            'created' : i.created
        }

        if i.voice:
            dat['voice'] = i.voice.url
        elif i.text:
            dat['text'] = i.text
        elif i.image:
            dat['image'] = i.image.url

        response['data'].append(dat)

    return Response(response)

@api_view(['POST'])
def send_message(request):
    response = {'status' : 200}
    sended_by_shop = request.data.get('sended_by_shop')

    chat = Chat.objects.get(pk=request.data.get('chat_id'))

    Message.objects.create(
            chat=chat,
            sended_by_shop=sended_by_shop,
            image=request.FILES.get('image') if 'image' in request.FILES else None,
            voice=request.FILES.get('voice') if 'voice' in request.FILES else None,
            text=request.data.get('message') if 'message' in request.data else None,
        )



    return Response(response)

@api_view(['GET'])
def get_or_create(request):
    response = {
            'status' : 200,
    }
    shop = Shop.objects.get(pk=request.GET.get('shop-id'))
    user = User.objects.get(pk=request.GET.get('user-id'))

    try:
        chat = Chat.objects.get(shop=shop, user=user)
        response['id'] = chat.id

    except Chat.DoesNotExist:
        new_chat = Chat.objects.create(shop=shop, user=user)
        response['id'] = new_chat.id

    return Response(response)

@api_view(['GET'])
def geo(request):
    response = {
        'status' : 200,
        'data' : []
    }

    lat = request.GET.get('lat')
    long = request.GET.get('long')

    min_distance = 10

    for i in Shop.objects.all():
        if distance.distance((lat, long), (i.lat, i.lon)).km < min_distance:
            response['data'].append(shop_serializer(i))


    return Response(response)


@api_view(['POST'])
def diamond(request):
    response = {
        'status' : 200,
    }

    try:
        user_id = request.data.get('user-id')

        user = User.objects.get(pk=user_id)
        user.diamond = user.diamond + 5
        user.save()

    except:
        response['status'] = 400


    return Response(response)

@api_view(['GET'])
def check_barcode(request):
    barcode = request.GET.get('barcode')
    for i in Product.objects.all():
        if i.barcode == barcode:
            return Response({'status' : 400})

    return Response({'status' : 200})
















