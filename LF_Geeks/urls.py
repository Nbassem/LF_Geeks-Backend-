"""LF_Geeks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    # login/ [for login]
    # register/ [to register user]
    # profile/ [user unique profile]
    path('', include('games.urls')),
    # creategame/ [to create game]
    # detailgame/ [to get game detail with guilds and memebers following]
    # gamelist/  [to get the list of games]
    path('', include('guilds.urls')),
    # guild/ [model view set to get list, detail, update, delete, create etcc the guild]
    # question_create[Create Questions]
    # question_update [Update questions]
    # question_list [Get questions]
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
