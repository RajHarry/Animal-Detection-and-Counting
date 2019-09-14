from django.contrib import admin 
from django.urls import path 
from django.conf import settings 
from django.conf.urls.static import static 
from . import views
  
urlpatterns = [ 
    path('image_upload', views.image_view, name = 'image_upload'), 
    path('success', views.success, name = 'success'),
    path('output_screen',views.output_screen,name='output_screen') 
] 

if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)