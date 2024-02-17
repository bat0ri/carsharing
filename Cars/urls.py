from django.contrib import admin
from django.urls import path, include
#from users import views as user_views
#from django.contrib.auth import views as auth_views
from catalog.views import index, catalog
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', index, name='home'),
    path('catalog/', include('catalog.urls', namespace='catalog')),
    path('users/', include('users.urls', namespace='users')),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
