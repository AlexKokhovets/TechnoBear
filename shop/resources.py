from django.http import JsonResponse
from .models import Category, Product
from .serializers import ProductSerializer, CategorySerializer
from rest_framework.decorators import api_view


@api_view(['GET'])
def get_products(request):
    products = Product.objects.filter(available=True)
    serializer = ProductSerializer(products, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def get_categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return JsonResponse(serializer.data, safe=False)
