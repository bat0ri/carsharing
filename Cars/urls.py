from django.contrib import admin
from django.urls import path, include
#from users import views as user_views
#from django.contrib.auth import views as auth_views
from catalog.views import index, catalog
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('register/', user_views.register, name='register'),
    #path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    #path('logout/', auth_views.LogoutView.as_view(template_name='car_list/main.html'), name='logout'),
    
    path('', index, name='home'),
    path('catalog/', catalog, name='catalog'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
