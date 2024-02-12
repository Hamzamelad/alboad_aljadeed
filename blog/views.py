from rest_framework import generics
from .models import Article
from .serializers import BlogSerializer

# Create your views here.
class BlogListView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = BlogSerializer

class BlogDetailView(generics.RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = BlogSerializer

