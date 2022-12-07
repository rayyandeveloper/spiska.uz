
url = 'https://spiska.pythonanywhere.com/api/product/'

data = {
    'shop_id': 11,
    'description' : 'descr',
    'name' : 'playground',
    'type' : 'dona',
    'count' : 15,
    'entry_price' : 10000,
    'price' : 10000, # new | o'zim qo'ygan narx
    'percent' : 50,
    'enterprise' : 'uz new star',
    'barcode' : 45789865,
    'selling_price' : 15000,
    'category' : '1-kategoriya' # new | kategoria
}

files = {
    'image1' : open('D:\Development\django\Spiska.uz\http\image.jpg', 'rb'),
    'image2' : open('D:\Development\django\Spiska.uz\http\image.jpg', 'rb'),
    'image3' : open('D:\Development\django\Spiska.uz\http\image.jpg', 'rb'),
}


