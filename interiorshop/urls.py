"""
URL configuration for interiorshop project.

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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings #??
from django.templatetags.static import static as fstatic# Not from django.conf.urls.static 
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls')),
    path('vendors/', include('apps.vendor.urls')),
    path('cart/', include('apps.cart.urls')),
    path('', include('apps.product.urls')),
    path('favicon.ico', RedirectView.as_view(url=fstatic('images/Favicon-32x32.png'))),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
