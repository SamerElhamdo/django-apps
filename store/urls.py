from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('list/', views.list_view, name='list_view'),
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
