from rest_framework.generics import ListAPIView , RetrieveAPIView
from .models import Post
from .serializers import PostSerializer


class PostAPI(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    
class PostDetailAPI(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer