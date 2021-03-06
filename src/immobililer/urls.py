"""immobililer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from authentication import views 
from django.conf import settings
from django.conf.urls.static import static
from immobililer.views import immobilier_home
from post_ad.views import post_ad_post_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', post_ad_post_list, name='home'),
    
    path('login/', views.LoginPage.as_view(), name="login"),
    path('singup/', views.SingupPage.as_view(), name="singup"),
    path('logout/', views.authentication_logout, name='logout'),
    path('delete/', views.DeleteAccount.as_view(), name='delete_user'),
    
    path('user/update/', views.EditInfo.as_view(), name='update_profile'),
    
    path("poster/", include("post_ad.urls"), name="poster"),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)