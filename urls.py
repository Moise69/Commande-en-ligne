from django.contrib import admin
from django.urls import path
from core import views as core_views
from orders import views as orders_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.menu, name='menu'),
    path('order/', orders_views.create_order, name='create_order'),
]
