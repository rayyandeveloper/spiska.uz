import requests as r
from shop import *


# url = 'https://spiska.pythonanywhere.com/api/shop/'


# data = {
#     'host-id': 18,
#     'name': 'Noutbuk shop',
#     'description': 'awdawdawdawd',
#     'password': '789awd',
#     'viloyat': 2,
#     'tuman': 3,
#     'lat': '70.95498434490544',
#     'lon': '40.52739341338905',
#     'currency ': '1',
#     'type': '2',
# }

# file = {
#     'image' : open('image.jpg', 'rb')
# }


json = r.post(url, data=data, files=files).json()


print(json)
