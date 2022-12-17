from django.urls import path
from . import views

app_name = 'nameapp'
urlpatterns = [
    path('', views.ProductListView.as_view(), name='all'),
    path('nameapp/<int:pk>/detail', views.ProductDetailView.as_view(), name='product_detail'),
    path('nameapp/create/', views.ProductCreateView.as_view(), name='product_create'),
    path('nameapp/<int:pk>/update/', views.ProductUpdateView.as_view(), name='product_update'),
    path('nameapp/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product_delete'),
    path('nameapp/<int:pk>/buy/', views.ProductBuyView.as_view(), name='product_buy'),
]
