from django.shortcuts import render
from datetime import datetime

def blog_details(request):
    post={
  "title":"My Second Templates Post",
  "description": "Django is a high level Python web framework that encourages rapid development and clean, pragmatic design."
  " Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without"
  " needing to reinvent the wheel. It’s free and open source.",
    "author": "Yes",
    "created_at": datetime(2026,10,27,21,16),
    "comments_count": 5,
    "tags": ["django", "python", "web development"],
    "price": 100,
    "number":10,
}
    return render(request, 'blog/blog_details.html', {"post":post})
