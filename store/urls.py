from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('new-product/', views.product_form, name='list_view'),
    path('new-order/<product_id>', views.order_form, name='order_form'),
    
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
