from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post
import datetime

# Create your views here.
def home(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 10)  # Show 10 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'index.html', {'posts': page_obj})

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})

def category_posts(request, category_slug):
    posts = Post.objects.filter(category__slug=category_slug)
    paginator = Paginator(posts, 10)  # Show 10 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/category_posts.html', 
                {'posts': page_obj, 
                'category_slug': category_slug
                })

def posts_author(request, author_username):
    posts = Post.objects.filter(author__username=author_username)
    paginator = Paginator(posts, 10)  # Show 10 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/author_posts.html', 
                {'posts': page_obj, 
                'author_username': author_username
                })

def archive_month(request, year, month):
    posts = Post.objects.filter(created_at__year=year, 
                                created_at__month=month
                            ).order_by('-created_at')
    month_date = datetime.date(year, month, 1)
    paginator = Paginator(posts, 10)  # Show 10 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/archive_month.html', 
                {'posts': page_obj, 
                'year': year,
                'month': month_date
                })