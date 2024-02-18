from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK, 
    HTTP_404_NOT_FOUND, 
    HTTP_201_CREATED, 
    HTTP_400_BAD_REQUEST
)

from .models import Product, Sku
from .serializers import ProductListSerializer, ProductDetailSerializer, SkuSerializer

@api_view(["PUT"])
@permission_classes([IsAdminUser])
def update_sku_status(request, pk):
    """
    Update the status of an SKU.
    """
    try:
        sku = Sku.objects.get(pk=pk)
    except Sku.DoesNotExist:
        return Response({"error": "SKU not found."}, status=HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serializer = SkuSerializer(sku, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
@api_view(["GET"])
@permission_classes([AllowAny])
def products_list(request):
    """
    List of all products.
    """

    products = Product.objects.all()
    serializer = ProductListSerializer(products, many=True)
    return Response({"products": serializer.data}, status=HTTP_200_OK)

@api_view(["GET"])
@permission_classes([AllowAny])
def product_detail(request, pk):
    """
    Retrieve details of a single product including its SKUs.
    """
    try:
        product = Product.objects.prefetch_related('skus').get(pk=pk)
    except Product.DoesNotExist:
        return Response({"error": "Product not found."}, status=HTTP_404_NOT_FOUND)
    
    serializer = ProductDetailSerializer(product)
    return Response(serializer.data, status=HTTP_200_OK)

@api_view(["POST"])
@permission_classes([IsAdminUser])
def create_sku(request):
    """
    Create a new SKU.
    """
    if request.method == 'POST':
        request.data['status'] = 0
        serializer = SkuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)