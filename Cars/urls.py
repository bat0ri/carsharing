from django.contrib import admin
from django.urls import path, include
#from users import views as user_views
#from django.contrib.auth import views as auth_views
from catalog.views import IndexView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', IndexView.as_view(), name='home'),
    path('catalog/', include('catalog.urls', namespace='catalog')),
    path('users/', include('users.urls', namespace='users')),
]

if settings.DEBUG:
    urlpatterns.append(path("__debug__/", include("debug_toolbar.urls")))
    
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
