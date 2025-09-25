from django.shortcuts import render, get_object_or_404
from .models import Category, ImagePrompt

def category_view(request, slug):
    category = get_object_or_404(Category, slug=slug)
    images = ImagePrompt.objects.filter(category=category).order_by('-created_at')
    categories = Category.objects.all()

    return render(request, 'gallery/category.html', {
        'category': category,
        'images': images,
        'categories': categories,  # to keep showing categories bar
    })


def index(request):
    # Fetch all categories (for categories bar)
    categories = Category.objects.all()

    # Fetch trending photos
    trending_photos = ImagePrompt.objects.filter(is_trending=True)

    context = {
        "categories": categories,
        "trending_photos": trending_photos,
    }
    return render(request, "gallery/index.html", context)

def image_detail(request, pk):
    image = get_object_or_404(ImagePrompt, pk=pk)
    return render(request, 'gallery/image_detail.html', {'image': image})




