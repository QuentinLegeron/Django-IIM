from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .models import Product

class ProductBaseView(View):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('nameapp:all')

class ProductListView(ProductBaseView, ListView):
    """View to list all products.
    Use the 'product_list' variable in the template
    to access all product objects"""

class ProductDetailView(ProductBaseView, DetailView):
    """View to list the details from one product.
    Use the 'Product' variable in the template to access
    the specific product here and in the Views below"""

class ProductCreateView(ProductBaseView, CreateView):
    """View to create a new product"""

class ProductUpdateView(ProductBaseView, UpdateView):
    """View to update a product"""

class ProductDeleteView(ProductBaseView, DeleteView):
    """View to delete a product"""

class ProductBuyView(ProductBaseView):
    """View to buy a product"""
    
    def get(self, request, *args, **kwargs):
        product = self.model.objects.get(pk=kwargs['pk'])
        product.stock -= 1
        product.save()
        return redirect('nameapp:all')
