"""config URL Configuration

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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from accounts import views
from shop import views
from config import settings

urlpatterns = [
    # path('', main, name='main_product_all'),
    # path('<slug:category_slug>/', views.main, name='main_category_all'),
    path('', views.main, name='main_product_all'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('shop/', include('shop.urls')),
    path('blog/', include('blog.urls')),
    path('cart/', include('cart.urls')),
    path('order/', include('order.urls')),
    path('coupon/', include('coupon.urls')),
    path('weather/', include('weather.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
