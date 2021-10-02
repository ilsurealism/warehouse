from django.urls import path
from .views import api_products, ProductsByCategoryList, ProductsByManufacturerList, product_detail, summary, summary_by_category
from .views import summary_by_manufacturer, index, ProductDetail


urlpatterns = [
    path('', index, name='index'),
    path('product/<str:code>/', ProductDetail.as_view(), name='product_detail'),
    # API
    path('electronics/all/', api_products),
    path('electronics/summary_by_category/<category>/', summary_by_category),
    path('electronics/summary_by_manufacturer/<manufacturer>/', summary_by_manufacturer),
    path('electronics/summary/', summary),
    path('electronics/<code>/', product_detail),
    path('electronics/category/<category>/', ProductsByCategoryList.as_view()),
    path('electronics/manufacturer/<manufacturer>/', ProductsByManufacturerList.as_view()),
]