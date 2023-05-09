from rest_framework.generics import ListAPIView ,ListCreateAPIView,RetrieveUpdateDestroyAPIView ,RetrieveAPIView ,UpdateAPIView,CreateAPIView,DestroyAPIView
from .models import Post
from .serializers import PostSerializer


class PostAPI(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    
class PostDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    
# class PostUpdateAPI(UpdateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
    
    
# class PostCreateAPI(CreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
    
    
# class PostDeleteAPi(DestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     # success_url = ''