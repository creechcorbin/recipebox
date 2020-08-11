"""recipebox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path

from recipes.views import index_view, post_detail, author_detail, add_recipe, add_author

urlpatterns = [
    path('', index_view, name="homepage"),
    path('post/<int:post_id>/', post_detail),
    path('author/<int:author_id>/', author_detail),
    path('addrecipe/', add_recipe, name="addrecipe"),
    path('addauthor/', add_author, name="addauthor"),
    path('admin/', admin.site.urls),
]
