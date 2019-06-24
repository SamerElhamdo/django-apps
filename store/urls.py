from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('control/login/', LoginView.as_view(template_name='control/control-login.html')),
    path('control/logout/', views.logout_view, name='logout'),
    path('control/home/', views.control_home, name='control_home'),
    path('control/list-product/', views.control_list_product, name='control_list_product'),
    path('control/add-product/', views.control_add_product, name='new_product'),
    path('control/edit-product/<product_id>', views.ProductUpdate.as_view(), name='edit_product'),
    path('control/delete-product/<product_id>', views.control_delete_product, name='delete_product'),
    path('control/add-product-attribute/<product_id>', views.control_add_product_attribute, name='add_product_attribute'),
    path('control/add-product-discount/<product_id>', views.control_add_product_discount, name='add_product_discount'),
    path('product-detail/<product_id>', views.product_detail, name='product_detail'),
    path('new-order/<product_id>', views.order_form, name='order_form'),
    
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
