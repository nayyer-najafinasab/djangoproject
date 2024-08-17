from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('' ,views.PostListView.as_view(), name = 'post_list') ,
    path('<int:pk>/details/' , views.PostDetailView.as_view(), name='post_detail') ,
    path('create/' , views.PostCreateView.as_view() , name ='post_create'),
    path('<int:pk>/update/' , views.PostUpdateView.as_view() , name = 'post_update'),
    path('<int:pk>/delete/' , views.PostDeleteView.as_view() , name = 'post_delete'),
]