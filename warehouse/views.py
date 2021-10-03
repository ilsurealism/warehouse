from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from django.views.generic.detail import DetailView

from .models import Product, Category, Manufacturer
from .serializers import ProductSerializer, ProductDetailSerializer, CategorySerializer, ManufacturerSerializer


def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'warehouse/index.html', context)


class ProductDetail(DetailView):
    model = Product
    template_name = 'warehouse/product_detail.html'
    context_object_name = 'product'
    slug_url_kwarg = 'code'
    slug_field = 'code'


# API
@api_view(['GET'])
def api_products(request):
    if request.method == 'GET':
        products = Product.objects.all()
        for product in products:
            gross_cost = product.quantity * product.price
            product.gross_cost = gross_cost
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def product_detail(request, code):
    try:
        product = Product.objects.get(code=code)
    except Product.DoesNotExist:
        return HttpResponse(status=406)

    if request.method == 'GET':
        serializer = ProductDetailSerializer(product)
        return Response(serializer.data)


class CreateProductAPIView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer



class UpdateProductAPIView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    lookup_url_kwarg = 'code'
    lookup_field = 'code'


class DeleteProductAPIView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    lookup_url_kwarg = 'code'
    lookup_field = 'code'


class CreateCategoryAPIView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class UpdateCategoryAPIView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class DeleteCategoryAPIView(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CreateManufacturerAPIView(CreateAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class UpdateManufacturerAPIView(UpdateAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class DeleteManufacturerAPIView(DestroyAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class ProductsByCategoryList(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category = self.kwargs['category']
        products = Product.objects.filter(category=category)
        for product in products:
            gross_cost = product.quantity * product.price
            product.gross_cost = gross_cost
        return products


class ProductsByManufacturerList(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        manufacturer = self.kwargs['manufacturer']
        products = Product.objects.filter(manufacturer=manufacturer)
        for product in products:
            gross_cost = product.quantity * product.price
            product.gross_cost = gross_cost
        return products


@api_view(['GET'])
def summary(request):
    products = Product.objects.all()
    summary = 0
    for product in products:
        summary += product.quantity
    return Response(summary)


@api_view(['GET'])
def summary_by_category(request, category):
    products = Product.objects.filter(category=category)
    summary = 0
    for product in products:
        summary += product.quantity
    return Response(summary)


@api_view(['GET'])
def summary_by_manufacturer(request, manufacturer):
    products = Product.objects.filter(manufacturer=manufacturer)
    summary = 0
    for product in products:
        summary += product.quantity
    return Response(summary)