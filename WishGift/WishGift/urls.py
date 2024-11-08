"""
URL configuration for WishGift project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from wishlist.views import index, item_delete, add_item
from authentication.views import login_page, logout_user, signup_page

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', login_page, name='login'),
    path('logout/', logout_user, name='logout'),
    path('signup/', signup_page, name='signup'),
    
    path('add-item/', add_item, name='add_item'),

    path('home/', index, name="home"),
    path('delete/<int:id>/', item_delete, name='delete'),
    # path('my-list/', mylist),
]
