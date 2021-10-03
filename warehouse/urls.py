from django.urls import path
from .views import api_products, ProductsByCategoryList, ProductsByManufacturerList, product_detail, summary, summary_by_category
from .views import summary_by_manufacturer, index, ProductDetail, CreateProductAPIView, UpdateProductAPIView, DeleteProductAPIView
from .views import CreateCategoryAPIView, UpdateCategoryAPIView, DeleteCategoryAPIView
from .views import CreateManufacturerAPIView, UpdateManufacturerAPIView, DeleteManufacturerAPIView

urlpatterns = [
    path('', index, name='index'),
    path('product/<str:code>/', ProductDetail.as_view(), name='product_detail'),
    # API
    path('electronics/all/', api_products),
    path('electronics/summary_by_category/<category>/', summary_by_category),
    path('electronics/summary_by_manufacturer/<manufacturer>/', summary_by_manufacturer),
    path('electronics/summary/', summary),
    path('electronics/<code>/', product_detail),
    path('electronics/product/create/', CreateProductAPIView.as_view()),
    path('electronics/product/update/<code>/', UpdateProductAPIView.as_view()),
    path('electronics/product/delete/<code>/', DeleteProductAPIView.as_view()),
    path('electronics/category/create/', CreateCategoryAPIView.as_view()),
    path('electronics/category/update/<int:pk>/', UpdateCategoryAPIView.as_view()),
    path('electronics/category/delete/<int:pk>/', DeleteCategoryAPIView.as_view()),
    path('electronics/manufacturer/create/', CreateManufacturerAPIView.as_view()),
    path('electronics/manufacturer/update/<int:pk>/', UpdateManufacturerAPIView.as_view()),
    path('electronics/manufacturer/delete/<int:pk>/', DeleteManufacturerAPIView.as_view()),
    path('electronics/category/<category>/', ProductsByCategoryList.as_view()),
    path('electronics/manufacturer/<manufacturer>/', ProductsByManufacturerList.as_view()),
]