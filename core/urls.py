
from . import views
from django.urls import path
urlpatterns = [
    
   path('core/',views.home,name='home'),
    path('about/',views.about,name='about'),
]