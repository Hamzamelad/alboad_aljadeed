from django.urls import path
from products.views import ListProductsView, ProductDetailView, TopProductsView, SimiListView
from blog.views import BlogListView, BlogDetailView
from messagesApp.views import MessageAPIView

urlpatterns = [
    path('blog', BlogListView.as_view()),
    path('blog/<int:pk>', BlogDetailView.as_view()),
    path('products', ListProductsView.as_view()),
    path('produts/<int:pk>', ProductDetailView.as_view()),
    path('products/top', TopProductsView.as_view()),
    path('products/simi', SimiListView.as_view()),
    path('message/', MessageAPIView.as_view()),
]
