from rest_framework import generics
from django.db.models import Q
from .models import Product
from .serializers import ProductSerializer


# Create your views here.
class ListProductsView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class TopProductsView(generics.ListAPIView):
    queryset = Product.objects.filter(id__in=[1,2,4,5,6])
    serializer_class = ProductSerializer

class SimiListView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(category=self.request.GET.get('cat')).exclude(id=self.request.GET.get('car'))


