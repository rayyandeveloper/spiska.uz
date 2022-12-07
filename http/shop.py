
url = 'https://spiska.pythonanywhere.com/api/shop/'
# url = 'http://127.0.0.1:8000/api/shop/'

files = {
    'image': open('D:\Development\django\Spiska.uz\http\image.jpg', 'rb')
}

data = {
    'host-id': 2,
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
