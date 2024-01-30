from .models import Category

def Categories(request):
    return {'categories': Category.objects.all()}