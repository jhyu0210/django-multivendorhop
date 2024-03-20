from django.urls import path
from django.contrib.auth import views as auth_views
#
#

from . import views

urlpatterns = [
    path('<slug:category_slug>/<slug:product_slug>/', views.product_details, name='product_details'),
    # path('contact/', views.contact, name='contact')
    path('<slug:category_slug>/',views.category, name="category")
]