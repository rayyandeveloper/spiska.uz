# Spiska.uz

----------

## Shop api
```
https://spiska.pythonanywhere.com/api/shop/
```

### GET

- #### Faqat bitta do'kon ma'lumotlarini olish uchun `id` beriladi
- #### Foydalanuvchining do'konlarini olish uchun `user-id` beriladi
- #### Do'konlarni qidirish uchun `q` beriladi
- #### Hech narsa berilmasa barcha do'kon ma'lumotlarini qaytaradi

### POST

- #### Do'kon yaratish uchun
```python 
files = {
    'image': open('http\image.jpg', 'rb')
}

data = {
    'host-id': 1,
    'name': 'test uz shop',
    'description': 'desc',
    'password': 'parol',
    'currency': 0,
    'type': 1,
    'viloyat': 2,
    'tuman': 3,
    'lat' : '45.66555',
    'lon' : '45.66555',
}
```
### PUT

- #### Do'kon ma'lumotlarini yangilash uchun `url` ga `id` qo'shiladi
```python 
files = {
    'image': open('http\image.jpg', 'rb')
}

data = {
    'name': 'test uz shop',
    'description': 'desc',
    'password': 'parol',
    'viloyat': 2,
    'tuman': 3,
    'lat' : '45.66555',
    'lon' : '45.66555',
}
```
### DELETE

- #### Do'konni o'chirish uchun `url` ga `id` qo'shiladi va `delete` request jo'natiladi

----------

## Product api
```
https://spiska.pythonanywhere.com/api/product/
```

### GET

- #### Faqat bitta mahsulot ma'lumotlarini olish uchun `id` beriladi
- #### Do'konning mahsulotlarini olish uchun `shop-id` beriladi
- #### Mahsulotlarni qidirish uchun `q` beriladi
- #### Hech narsa berilmasa barcha mahsulot ma'lumotlarini qaytaradi
- #### Viloyat bo'yicha saralash uchun `region` beriladi
- #### Tuman bo'yicha saralash uchun `district` beriladi
- #### Tuman va Viloyat bo'yicha saralash uchun `region` va `district` beriladi

### POST

- #### Mahsulot yaratish uchun
```python 
data = {
    'shop_id': 1,
    'description': 'descr',
    'name': 'playground',
    'type': 'dona',
    'count': 15,
    'entry_price': 10000,
    'price': 10000,  # new | o'zim qo'ygan narx
    'percent': 50,
    'enterprise': 'uz new star',
    'barcode': 45789865,
    'selling_price': 15000,
    'category': '1-kategoriya'  # new | kategoria
}

files = {
    'images': [
        open('D:\Development\django\Spiska.uz\http\image.jpg', 'rb'),
        open('D:\Development\django\Spiska.uz\http\image.jpg', 'rb'),
        open('D:\Development\django\Spiska.uz\http\image.jpg', 'rb'),
    ]
}
```
### PUT

- #### Do'kon ma'lumotlarini yangilash uchun `url` ga `id` qo'shiladi
```python 
files = {
    'image': open('http\image.jpg', 'rb')
}

data = {
    'name': 'test uz shop',
    'description': 'desc',
    'password': 'parol',
    'viloyat': 2,
    'tuman': 3,
    'lat' : '45.66555',
    'lon' : '45.66555',
}
```
### DELETE

- #### Do'konni o'chirish uchun `url` ga `id` qo'shiladi va `delete` request jo'natiladi

----------


