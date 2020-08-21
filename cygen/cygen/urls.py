"""cygen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from app1 import views
from django.conf.urls.static import static
from cygen import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.showIndex, name="main"),
    path('emp_register/', views.emp_register,name="emp_register"),
    path('save_register/', views.save_register,name="save_register"),
    path('emp_login/', views.emp_login,name="emp_login"),
    path('login_check/', views.login_check,name="login_check"),
    path('cygen_home/', views.cygen_home,name="cygen_home"),
    path('cygen_add/', views.cygen_add,name="cygen_add"),
    path('save_service/', views.save_service,name="save_service"),
    path('view_service/', views.view_service,name="view_service"),
    path('show_update/', views.show_update,name="show_update"),
    path('update_ser/', views.update_ser,name="update_ser"),
    path('delete_emp/', views.delete_emp,name="delete_emp"),
    path('emp_logout/', views.emp_logout,name="emp_logout"),





]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)