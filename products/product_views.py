from django.http.response import JsonResponse
from rest_framework.decorators import api_view, throttle_classes
from rest_framework.parsers import JSONParser
from rest_framework import status

from .models import Product
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.throttling import UserRateThrottle

class CustomRateThrottle(UserRateThrottle):
    rate = '100/day'    # 100 solicitudes por dia

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
@throttle_classes([CustomRateThrottle])
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()    # Listamos todos los productos

        # Filtrar por nombre de producto
        name = request.GET.get('name', None)
        if name is not None:
            products = products.filter(product_name__icontains=name) # Filtramos por nombre de la lista de productos anterior

        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        product_data = JSONParser().parse(request)
        serializer = ProductSerializer(data=product_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
@throttle_classes([CustomRateThrottle])
def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk) # Verificamos si existe el producto
    except:
        return JsonResponse({'message':'El producto no existe.'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(product) # Si el producto existe lo serializa
        return JsonResponse(serializer.data)    # Lo envía como respuesta

    elif request.method == 'PUT':
        product_data = JSONParser().parse(request) # Parsea el request enviado a formato JSON
        serializer = ProductSerializer(product, data=product_data) # esto que hace?
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        product.delete()
        return JsonResponse({'message':'El producto fue eliminado con exito.'}, status=status.HTTP_204_NO_CONTENT)


class CustomRateThrottle(UserRateThrottle):
    rate = '100/day'    # 100 solicitudes por dia