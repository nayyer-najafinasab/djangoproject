from django.shortcuts import render , get_object_or_404 , redirect
from django.urls import reverse_lazy
from django.views import generic

from .models import Post

from . forms import NewPostForm


# Create your views here.


# def post_list(request) :
#     # posts = Post.objects.all(
#     posts = Post.objects.filter(status = 'pub').order_by('-update_date')
#     return render(request , 'blog/post_list.html' , {'posts' : posts})





class PostListView(generic.ListView):
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    def get_queryset(self):
        return Post.objects.filter(status='pub').order_by('-update_date')






# def post_detail_view(request ,id) :
#     # post = Post.objects.get(id = id)
#     post = get_object_or_404(Post , id =id)
#     return render(request , 'blog/post_detail.html' ,{'post' : post})

class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

# def post_create_view(request):
#     # if request.method == 'POST' :
#     #     post_title = request.POST.get('title')
#     #     post_text = request.POST.get('text')
#     #
#     #     Post.objects.create(title = post_title ,discription = post_text , status='drf' )
#     #     return redirect('blog:post_list')
#     # else :
#     #     print(request.method)
#     if request.method == 'POST' :
#         form = NewPostForm(request.POST)
#         if form.is_valid() :
#             form.save()
#             return redirect("blog:post_list")
#
#     else:
#         form = NewPostForm()
#     return render(request , 'blog/post_craete.html' , {'form' :form})

class PostCreateView(generic.CreateView):
    form_class = NewPostForm
    template_name = 'blog/post_craete.html'
# def post_update_view(request , id):
#     post = get_object_or_404(Post , id=id)
#     form = NewPostForm(request.POST or None , instance=post)
#     if form.is_valid():
#         form.save()
#         return redirect('blog:post_list')
#
#     return render(request , 'blog/post_craete.html' ,{'form':form})

class PostUpdateView(generic.UpdateView):
    model = Post
    form_class =NewPostForm
    template_name = 'blog/post_craete.html'



# def post_delete_view(request , id) :
#     post = get_object_or_404(Post , id=id)
#     if request.method == 'POST' :
#         post.delete()
#         return redirect('blog:post_list')
#     return render(request , 'blog/post_delete.html' ,{'post':post})



class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy( 'blog:post_list')



















