from django.shortcuts import render,get_object_or_404,redirect 
from .models import Post 
from .forms import PostForm
#from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

def post_list(request):
	posts = Post.objects.filter(published_date__isnull=False).order_by('published_date')
	return render(request,'blog/post_list.html',{'posts':posts})

def post_detail(request,pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html',{'post':post})

@login_required
def post_edit(request,pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST": 
		form = PostForm(request.POST,instance=post)
		if form.is_valid():
			post = form.save(commit=False)			
			me = User.objects.get(username='root')
			post.author = request.user()
			post.save()
			return redirect('blog.views.post_detail',pk=post.pk)
	else:
		form = PostForm(instance=post)
	return render(request,'blog/post_edit.html',{'form':form})

@login_required
def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			me = User.objects.get(username='root')
			post.author = request.user()
			post.save()
			return redirect('blog.views.post_detail',pk=post.pk)
	else :
		form = PostForm()
 
	return render(request, 'blog/post_edit.html',{'form':form})
