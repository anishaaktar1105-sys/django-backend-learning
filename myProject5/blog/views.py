from django.shortcuts import render
from  datetime import datetime

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def home(request):
    context = {
        'name': 'Anisha',
        'age': 21,
        'skills': ['Python', 'Django', 'JavaScript'],
        'user': User('Anu', 25),
        'blogs': {
            'title': 'Django Template Intro',
            'author': {
            'name': 'Anisha',
         
            },
            'content': '<b>Django templates are a powerful way to generate dynamic HTML content. </b>'
            'They allow you to separate the presentation logic from the business logic, making your code cleaner and more maintainable.',
            'created_at': datetime(2026,10,24,17,14),
        },
        'empty_value': None,
    }
    return render(request, 'blog/home.html', context)