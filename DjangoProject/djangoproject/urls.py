from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls')),
]

#urlpatterns+= staticfiles_urlpatterns()