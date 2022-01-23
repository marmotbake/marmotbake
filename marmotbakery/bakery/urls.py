#from asyncio.windows_events import NULL
from django.urls import path
from . import views
#from django.conf import settings 
#from django.conf.urls.static import static 
from django.shortcuts import render


urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("placeorder", views.placeorder, name="placeorder"),
    path("myorders", views.myorders, name="myorders"),
    path("waitlist", views.waitlist, name="waitlist"),
    path("edit/<int:id>", views.edit, name="edit"),
    path("delete/<int:id>", views.delete, name="delete"),
    path("taskmanager", views.taskmanager, name="taskmanager"),
    path("metrics", views.metrics, name="metrics"),
    path("blogadmin", views.blogadmin, name="blogadmin"),
    path("deleteuser/<int:id>", views.deleteuser, name="deleteuser"),
    path("blog", views.blog, name="blog"),
    path("fileupload/<int:id>", views.fileupload, name="fileupload"),
    path("contententry/<int:blogid>", views.contententry, name="contententry"),
    path("createblog/<int:blogid>", views.createblog, name="createblog"),
    path("blogdetails/<int:blogid>", views.blogdetails, name="blogdetails"),
    path("deleteblog/<int:blogid>", views.deleteblog, name="deleteblog"),
    path("editblog/<int:blogid>", views.editblog, name="editblog"),
    
    path('bread_white', lambda request: render(request, 'bakery/bread_white.html')),
    path('bread_country', lambda request: render(request, 'bakery/bread_country.html')),
    path('bread_oats', lambda request: render(request, 'bakery/bread_oats.html')),
    path('bread_semolina', lambda request: render(request, 'bakery/bread_semolina.html')),
    path('bread_wholeweed', lambda request: render(request, 'bakery/bread_wholeweed.html')),
    path('bread_seeded', lambda request: render(request, 'bakery/bread_seeded.html')),
    path('bread_baguette', lambda request: render(request, 'bakery/bread_baguette.html')),
    path('bread_sweet', lambda request: render(request, 'bakery/bread_sweet.html')),

] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


