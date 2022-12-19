from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Phone

@api_view(['GET'])
def change(request):
    return Response({'status' : 200, 'phone' : f"{Phone.objects.get(pk=1).number}"})



