from .models import Category
from django.db.models.functions import TruncMonth
from django.db.models import Count
from .models import Post

def categories_processor(request):
    """ Retornara todas las categorias ordenadas por ID. En el template
    para usarla en menu global. """
    categories = Category.objects.all().order_by('id')
    return {'categories': categories}

def archive_months(request):
    """ Retornara una lista de meses con posts publicados para
    usar en el template como archivo mensual. """
    archives = (Post.objects
                .filter(published=True)
                .annotate(month=TruncMonth('created_at'))
                .values('month')
                .annotate(post_count=Count('id'))
                .order_by('-month'))
    
    formatted_archive = []
    for item in archives:
        formatted_archive.append({
            'month_date': item['month'],
            'count': item['post_count']
        })
    return {'archive_months': formatted_archive}