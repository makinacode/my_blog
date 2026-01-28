from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('category/<slug:category_slug>/', views.category_posts, name='category_posts'),
    path('author/<str:author_username>/', views.posts_author, name='posts_author'),
    path('archive/<int:year>/<int:month>/', views.archive_month, name='archive_month'),
]