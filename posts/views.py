from django.shortcuts import render , redirect
from .models import Post , Author
from .forms import PostForm


def post_list(request):
    data = Post.objects.all()   # select * from Post
    return render(request,'posts.html',{'posts':data})



def post_detail(request,post_id):
    data = Post.objects.get(id=post_id)
    return render(request,'detail.html',{'post':data})


def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            author = Author.objects.get(user=request.user)
            myform.author = author
            myform.save()
            return redirect('/blog')
    else:
        form = PostForm()
    return render(request,'new.html',{'form':form})