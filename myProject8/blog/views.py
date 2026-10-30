from django.shortcuts import render
from datetime import datetime


def blog_list(request):
    blogs=[
        {"title": "Django Basics", "is_featured": True, "date_posted": datetime(2024, 6, 1)},
    ]
    context = {
        "blogs":blogs,
    }
    return render(request, 'blog/blog_list.html', context)
