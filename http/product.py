
url = 'https://spiska.pythonanywhere.com/api/product/'

data = {
    'shop_id': 11,
    'description' : 'descr',
    'name' : 'playground',
    'type' : 'dona',
    'count' : 15,
    'entry_price' : 10000,
    'percent' : 50,
    'enterprise' : 'uz monkey',
    'barcode' : 45789865,
    'selling_price' : 15000

}

files = {
    'image1' : open('D:\Development\django\Spiska.uz\http\image.jpg', 'rb'),
    'image2' : open('D:\Development\django\Spiska.uz\http\image.jpg', 'rb'),
    'image3' : open('D:\Development\django\Spiska.uz\http\image.jpg', 'rb'),
}


