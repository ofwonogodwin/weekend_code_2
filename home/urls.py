from django.urls import path
from.import views

## url patterns.

urlpatterns = [
    path('',views.home,name='homepage'),
    path('about/',views.about,name='aboutpage'),
    path('gallery/',views.gallery,name='gallerypage'),
    path('contact/',views.contact,name='contactpage'),
]