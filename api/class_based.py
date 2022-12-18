from rest_framework.response import Response
from rest_framework.views import APIView
from api import *
from home.models import *
from django.db.models import Q 

import random as r 

def check_image(list1, i):
    try:
        return list1[i]
    except:
        return None



class ShopAPIView(APIView):
    def get(self, request):
        response = {
            'status': 200,
            'data': []
        }

        pk = request.GET.get('id')
        userId = request.GET.get('user-id')
        
        q = request.GET.get('q')


        if pk:
            try:
                obj = Shop.objects.get(pk=pk)

                response['data'] = [shop_serializer(obj)]

            except Shop.DoesNotExist:
                response['status'] = 400
        elif userId:
            try:
                user = User.objects.get(pk=userId)

                response['creator'] = [shop_serializer(u) for u in Shop.objects.filter(host=user)]
                response['admin'] = [shop_serializer(u) for u in Shop.objects.filter(admins=user)]
                response['user'] = [shop_serializer(u) for u in Shop.objects.filter(members=user)]

            except User.DoesNotExist:
                response['status'] = 400
        elif q:
            response['data'].append(shop_serializer(shop) for shop in Shop.objects.filter(Q(name__icontains=q) | Q(bio__icontains=q)))

        else: 
            response['data'] = [shop_serializer(obj) for obj in Shop.objects.all()]
            

        return Response(response)

    def post(self, request):
        response = {'status': 400, 'message' : '', 'diamonds' : 0}
        rd = request.data
        try:
            host:User = User.objects.get(pk=rd['host-id'])
            name = rd['name']
            desc = rd['description']
            password = rd['password']
            currency = rd['currency']
            type = rd['type']
            pk1 = int(rd['viloyat'])
            pk2 = int(rd['tuman'])
            img = request.FILES['image']
            viloyat = Region.objects.get(pk=pk1)
            tuman = District.objects.get(pk=pk2)

   

            lat = rd['lat']
            lon = rd['lon']

            if host.diamond < 400:
                response['status'] = 400
                response['message'] = 'Lack of diamonds'
                response['diamonds'] = 400 - host.diamond


            else:
                new_shop = Shop.objects.create(
                    host=host,
                    name=name,
                    type=type,
                    currency=currency,
                    dollar_currency=0,
                    bio=desc,
                    password=password,
                    viloyat=viloyat,
                    tuman=tuman,
                    image=img,
                    lat=lat,
                    lon=lon
                )

                host.diamond = host.diamond - 400
                host.save()

                for i in range(1, 16, 1):
                    Category.objects.create(
                        shop=new_shop,
                        name=f"{i}-kategoriya"
                    )

                response['status'] = 200
        except Exception as e:
            print('Shop create error, ', e)

        return Response(response)

    def delete(self, request):
        pk = request.GET.get('id')
        response = {
            'status': 200,
        }

        try:
            shop: Shop = Shop.objects.get(pk=pk)
            shop.delete()
            response['status'] = 200
        except Shop.DoesNotExist:
            response['status'] = 404

        return Response(response)

    def put(self, request):
        pk = request.GET.get('id')
        response = {
            'status': 200,
        }

        rd = request.data
        try:
            shop = Shop.objects.get(pk=pk)
            shop.name = rd['name']
            shop.bio = rd['description']
            shop.password = rd['password']
            shop.viloyat = Region.objects.get(pk=int(rd['viloyat']))
            shop.tuman = District.objects.get(pk=int(rd['tuman']))
            shop.image = request.FILES['image']
            shop.lat = rd['lat']
            shop.lon = rd['lon']

            shop.save()


        except Shop.DoesNotExist:
            response['status'] = 404

        return Response(response)


class ProductAPIView(APIView):
    def get(self, request):
        response = {
            'status': 200,
            'data': []
        }
        
        pk = request.GET.get('id')
        q = request.GET.get('q')
        district = request.GET.get('district')
        region = request.GET.get('region')
        shop_id = request.GET.get('shop-id')

        if pk:
            try:
                obj = Product.objects.get(pk=pk)

                barcode = obj.barcode
                products_list = Product.objects.filter(barcode=barcode)


                response['data'] = [special_product_serializer(products_list[0], products_list)]

            except Product.DoesNotExist:
                response['status'] = 400
        elif shop_id:
            response['data'] = [product_serializer(obj) for obj in Product.objects.filter(shop__id=shop_id)]

        elif q:
            response['data'] = [product_serializer(obj) for obj in Product.objects.filter(Q(name__icontains=q) | Q(description__icontains=q) | Q(company__icontains=q))]

        elif region:
            response['data'] = [product_serializer(obj) for obj in Product.objects.filter(shop__viloyat__id=region)]
            
        elif region and district:
            response['data'] = [product_serializer(obj) for obj in Product.objects.filter(Q(shop__viloyat__id=region) | Q(shop__tuman__id=district))]
            
        else: 
            response['data'] = [product_serializer(obj) for obj in Product.objects.all()]
            

        return Response(response)

    def post(self, request):
        response = {
            'status': 200,
        }

        type = {
            'dona' : '1',
            'litr' : '2',
            'm2' : '3'
        }

        currency = {0 : '1', 1 : '2'}

        try:
            rd = request.data

            shop = Shop.objects.get(pk=rd['shop_id'])

            image1 = check_image(request.FILES['images'], 0)
            image2 = check_image(request.FILES['images'], 1)
            image3 = check_image(request.FILES['images'], 2)


            new_product = Product.objects.create(
                shop=shop,
                image1=image1,
                image2=image2,
                image3=image3,
                name=rd['name'],
                description=rd['description'],
                category=Category.objects.get(name=rd['category'], shop=shop),
                type=type[rd['type']],
                currency=currency[shop.currency],
                price_in_dollar=float(str(int(rd['price']) / shop.dollar_currency)[:5]),
                count=rd['count'],
                dollar_currency=shop.dollar_currency,
                company=rd['enterprise'],
                entry_price=rd['entry_price'],
                price=rd['price'],
                percent=rd['percent'],
                selling_price=rd['selling_price'],
                barcode=rd['barcode']
            )


        except KeyError as e:
            print(e)
            response['status'] = 400
        except Exception as e:
            print(e)

        return Response(response)

    def delete(self, request):
        pk = request.GET.get('id')
        response = {
            'status': 200,
        }

        try:
            product: Product = Product.objects.get(pk=pk)

            product.delete()

            response['status'] = 200
        except Shop.DoesNotExist:
            response['status'] = 404

        return Response(response)

    def put(self, request):
        pk = request.GET.get('id')
        response = {
            'status': 200,
        }

        type = {
            'dona' : '1',
            'litr' : '2',
            'm2' : '3'
        }

        currency = {"so'm" : '1', 'dollar' : '2'}


        try:

            rd = request.data

            product: Product = Product.objects.get(pk=pk)
            product.image1 = request.FILES['image1']
            product.image2 = request.FILES.get('image2', None)
            product.image3 = request.FILES.get('image3', None)
            product.name = rd['name']
            product.description = rd['description']
            product.count = rd['count']
            product.type = type[rd['type']],
            product.currency = currency[rd['currency']],
            product.entry_price = rd['entry_price']
            product.percent = rd['percent']
            product.selected = rd['selected']
            product.selling_price = rd['selling_price']

            product.save()
        except Product.DoesNotExist:
            response['status'] = 404
        return Response(response)


class EProductAPIView(APIView):
    def get(self, request):
        response = {
            'status': 200,
            'data': []
        }
        
        pk = request.GET.get('id')
        q = request.GET.get('q')
        district = request.GET.get('district')
        region = request.GET.get('region')
        shop_id = request.GET.get('shop-id')

        if pk:
            try:
                obj = EProduct.objects.get(pk=pk)

                response['data'] = [eproduct_serializer(obj)]

            except Product.DoesNotExist:
                response['status'] = 400
        elif shop_id:
            response['data'] = [eproduct_serializer(obj) for obj in EProduct.objects.filter(shop__id=shop_id)]

        elif q:
            response['data'] = [eproduct_serializer(obj) for obj in EProduct.objects.filter(Q(name__icontains=q) | Q(description__icontains=q) | Q(company__icontains=q))]

        elif region:
            response['data'] = [eproduct_serializer(obj) for obj in EProduct.objects.filter(shop__region__id=region)]
            
        elif region and district:
            response['data'] = [eproduct_serializer(obj) for obj in EProduct.objects.filter(Q(shop__region__id=region) | Q(shop__district__id=region))]
            
        else: 
            response['data'] = [eproduct_serializer(obj) for obj in EProduct.objects.all()]
            

        return Response(response)

    def post(self, request):
        response = {
            'status': 200,
        }

        type = {
            'dona' : '1',
            'litr' : '2',
            'm2' : '3'
        }

        currency = {0 : '1', 1 : '2'}

        try:
            rd = request.data

            shop = Shop.objects.get(pk=rd['shop_id'])
            
            image1 = check_image(request.FILES['images'], 0)
            image2 = check_image(request.FILES['images'], 1)
            image3 = check_image(request.FILES['images'], 2)


            new_product = EProduct.objects.create(
                shop=shop,
                image1=image1,
                image2=image2,
                image3=image3,
                name=rd['name'],
                dollar_currency=shop.dollar_currency,
                category=Category.objects.get(name=rd['category'], shop=shop),
                type=type[rd['type']],
                currency=currency[shop.currency],
                selling_price=rd['selling_price'],
                barcode=rd['barcode']
            )
            

        except KeyError as e:
            print(e)
            response['status'] = 400
        except Exception as e:
            print(e)

        return Response(response)

    def delete(self, request):
        pk = request.GET.get('id')
        response = {
            'status': 200,
        }

        try:
            product: EProduct = EProduct.objects.get(pk=pk)

            product.delete()

            response['status'] = 200
        except EProduct.DoesNotExist:
            response['status'] = 404

        return Response(response)

    def put(self, request):
        pk = request.GET.get('id')
        response = {
            'status': 200,
        }

        type = {
            'dona' : '1',
            'litr' : '2',
            'm2' : '3'
        }

        currency = {"so'm" : '1', 'dollar' : '2'}


        try:

            rd = request.data

            product: EProduct = EProduct.objects.get(pk=pk)
            product.image1 = request.FILES['image1']
            product.image2 = request.FILES.get('image2', None)
            product.image3 = request.FILES.get('image3', None)
            product.name = rd['name']
            product.type = type[rd['type']],
            product.selling_price = rd['selling_price']
            product.save()
        except EProduct.DoesNotExist:
            response['status'] = 404
        return Response(response)


class UserAPIView(APIView):
    def get(self, request):
        pk = request.GET.get('id')
        q = request.GET.get('q')
        phone = '+' + request.GET.get('phone')[1:] if request.GET.get('phone') else None
        response = {
            'status': 200,
            'data': []
        }
        
        if pk:
            try:
                user = User.objects.get(pk=pk)
                response['data'].append(user_serializer(user))

            except User.DoesNotExist:
                print('User pk get failed')
                response['status'] = 400
        elif q:
            response['data'] = [user_serializer(user) for user in User.objects.filter(Q(first_name__icontains=q) | Q(last_name__icontains=q))]

        elif phone:
            try:
                user = User.objects.get(phone=phone)
                response['data'].append(user_serializer(user))

            except User.DoesNotExist:
                print('User phone get failed')
                response['status'] = 400

        else: 
            try:
                response['data'] = [user_serializer(user) for user in User.objects.all()]
            except Exception as e:
                print(e)

        return Response(response)

    def post(self, request):
        rd = request.data
        response = {'status': 200}
        try:
            new_user = User.objects.create_user(
                username = rd['first_name'] + rd['last_name'],
                first_name=rd['first_name'],
                last_name=rd['last_name'],
                diamond=1000,
                phone=rd['phone'],
                img=request.FILES['image']
            )

        except Exception as e:
            print(e)
            response['status'] = 400

        return Response(response)

    def delete(self, request):
        pk = request.GET.get('id')
        response = {'status': 200}

        try:
            user: User = User.objects.get(pk=pk)
            user.delete()
            response['status'] = 200

        except User.DoesNotExist:
            response['status'] = 404

        return Response(response)


    def put(self, request):
        pk = request.GET.get('id')
        response = {
            'status': 200,
            'data': []
        }

        rd = request.data
        try:
            user: User = User.objects.get(pk=pk)

            user.first_name = rd['first_name']
            user.last_name = rd['last_name']
            # user.phone = rd['phone']
            user.img = request.FILES['image']

            user.save()

            response['data'].append(
                {
                    'id': user.id,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'phone': user.phone,
                    'img': user.img.url,
                }
            )
        except User.DoesNotExist:
            response['status'] = 404

        return Response(response)


class PromocodeAPIView(APIView):
    def get(self, request):
        shop_id = request.GET.get('shop-id')
        
        response = {
            'status' : 200,
            'data' : []
        }
        
        if shop_id:
            response['data'] = [{'percent' : obj.percent, 'code' : obj.code, 'products' : [product_serializer(o) for o in obj.products.all()]} for obj in Promocode.objects.filter(shop__id=shop_id)]
        
        return Response(response)

    def post(self, request):
        response = {
                'status' : 200,
            }
        try:
            shop = Shop.objects.get(pk=request.data.get('shop-id'))
            percent = request.data.get('percent')

            
            code = f'{CHARS[r.randint(1, 26)]}{CHARS[r.randint(1, 26)]}{CHARS[r.randint(1, 26)]}{CHARS[r.randint(1, 26)]}{CHARS[r.randint(1, 26)]}{CHARS[r.randint(1, 26)]}'
            
            while check_promocode(code):
                code = f'{CHARS[r.randint(1, 26)]}{CHARS[r.randint(1, 26)]}{CHARS[r.randint(1, 26)]}{CHARS[r.randint(1, 26)]}{CHARS[r.randint(1, 26)]}{CHARS[r.randint(1, 26)]}'
            
            new_promocode = Promocode.objects.create(
                shop=shop,
                percent=percent,
                code=code
            )

            for i in request.data.get('products'):
                new_promocode.products.add(Product.objects.get(pk=i))

        except Exception as e:
            print(e)
            response['status'] = 400
            
        return Response(response)
            
    def delete(self, request):
        pk = request.GET.get('id', None)
        print(pk)
        if pk:
            try:
                Promocode.objects.get(pk=pk).delete()
                return Response({'status' : 200})
            except:
                return Response({'status' : 400})
        return Response({'status' : 400})

