from rest_framework.generics import ListAPIView , RetrieveAPIView ,UpdateAPIView,CreateAPIView,DestroyAPIView
from .models import Post
from .serializers import PostSerializer


class PostAPI(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    
class PostDetailAPI(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    
class PostUpdateAPI(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    
class PostCreateAPI(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    
class PostDeleteAPi(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # success_url = ''