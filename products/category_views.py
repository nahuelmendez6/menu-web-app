from django.core.serializers import serialize
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view, throttle_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.throttling import UserRateThrottle

from .models import Category
from .serializers import CategorySerializer
class CustomRateThrottle(UserRateThrottle):
    rate = '100/day'    # 100 solicitudes por dia

"""
Endpoint para listar y crear categorias
"""
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
@throttle_classes([CustomRateThrottle])
def category_list(request):
    if request.method == 'GET':
        categories = Category.objects.all()

        # Filtrar por nombre (opcional)
        name = request.GET.get('name', None)
        if name is not None:
            categories = categories.filter(category_name__icontains=name)

        serializer = CategorySerializer(categories, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        category_data = JSONParser().parse(request)
        serializer = CategorySerializer(data=category_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""
Endpoint para detalles de categoria
"""
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
@throttle_classes([CustomRateThrottle])
def category_detail(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExists:
        return JsonResponse({'message':'La categoría no existe'}, status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        category_data = JSONParser().parse(request)
        serializer = CategorySerializer(category, data=category_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        category.delete()
        return JsonResponse({'message':'La categoría fue eliminada exitosamente'})


